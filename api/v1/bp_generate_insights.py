#!/usr/bin/env python3

"""generage insights from user's entries using Chatgpt API"""

import openai
import os
from datetime import datetime, timezone, timedelta
from .utilities import storage
from flask import Blueprint, request, redirect, url_for, g

openai.apikey = os.getenv('OPENAI_API_KEY')

generate_insight_handler = Blueprint('generate_insight_handler', __name__,
                                  url_prefix='/insight')

@generate_insight_handler.route('/', methods=['POST', 'GET'])
def generate_insight():
    """generate insights for a user's entries using
    chatgpt api and return them"""
    if not g.user:
        return redirect(url_for('login'))

    if request.method == 'GET':
        start_date = get_start_date()
        end_date = datetime.now(tz=timezone.utc).isoformat()
        user_entries_string = fetch_entries(start_date, end_date)
        generated_insight = generate_insight(user_entries_string)

        result = save_insight(generated_insight, start_date, end_date)

        return result

    if request.method == 'POST':
        if not request.json:
            return {'Error': 'invalid json input'}, 400

        data = reqeust.json
        start_date = data['start_date']
        end_date = data['end_date']
        user_entries_string = fetch_entries(start_date, end_date)
        generated_insight = generate_insight(user_entries_string)

        result = save_insight(generated_insight, start_date, end_date)

        return result


def get_start_date():
    """Calculate and return(as an ISO string) the first day of
    the month for filtering user entries that will be used to
    generate insight"""

    current_time = datetime.now(tz=timezone.utc)
    interval = timedelta(days=current_time.day - 1, hours=current_time.hour,
                         minutes=current_time.minute,
                         seconds=current_time.second,
                         microseconds=current_time.microsecond - 0.5)
    start_date = current_time - interval
    return start_date.isoformat()


def fetch_entries(start_date, end_date):
    """fetch all of a user's entries from the database that were created
    earlier than start_date and later than end_date and
    concatenate them"""

    # convert datetime string to datetime objects
    start_date = datetime.fromisoformat(start_date)
    end_date = datetime.fromisoformat(end_date)

    all_entries = storage.all_user_entries(g.user.id)
    all_entries = [list(entry)[0] for entry in all_entries]
    filtered_entries = [
        entry for entry in all_entries if (entry.created_at >= start_date
        and entry.created_at <= end_date)]

    # at this point, filtered_entries is a list of entry objects.
    # the entry strings still have to be extracted

    all_entry_string = ''

    for entry in filtered_entries:
        all_entry_string += entry.entry + '\n\n\n'
        all_entry_string = all_entry_string.strip()

    return all_entry_string


def analyse_entries(entries_string):
    """use gpt 3.5 turbo to analyse a string containing
    all entries and return the generated insight"""

    prompt = """I want you to analyze a series of journal entries I have
    written and draw insights from them based on the content of the entries.
    Consider the details of what I'm saying in each entry and group insights
    into different categories based on the content, such as finances, hopes,
    gratitude, or any other relevant categories that emerge from the entries.
    The entries are separated by two or more blank lines, and you'll use the
    content of the entries to provide insights about different aspects of my
    life as mentioned in the journal. Your insights shouldn't be a day-to-day
    analysis of each entry, but an aggregation of insights from all entries."""

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': entries_string},
            {'role': 'user', 'content': entries_string}
        ]
    )

    insight = response['choices'][0]['message']['content']

    return insight


def save_insight(insight, start_date, end_date):
    """Save the generated insight to the database and return
    the stored version of the database"""

    Insight = storage.classes['Insights']

    new_insight = Insight(user_id=g.user.id, start_date=start_date,
                          end_date=end_date, insight=insight)
    storage.add(new_insight)
    storage.save()

    all_insights = storage.all_user_insights(g.user.id)
    latest_insight = list(all_insights[-1]).to_dict()

    return latest_insight
