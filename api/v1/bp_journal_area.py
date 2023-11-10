#!/usr/bin/env python3
"""Implement the journal area, where a user sees their entries for
   the current month and can make new entries"""

from flask import request, g, Blueprint, redirect, url_for
from .utilities import storage
from datetime import timedelta, datetime, timezone

journal_area_handler = Blueprint('journal_area_handler', __name__)

@journal_area_handler.route('/<username>/entries',
                         methods=['GET', 'POST', 'PATCH', 'DELETE'])

def journal_area(username):
    """Handle the main chat area view of the application where users can
       can see their entries for the last 30 days and make new ones
    """
    if not g.user:
        return redirect(url_for('app_views.login_handler.login'))

    if request.method == 'GET':
        current_month_journals = current_month_journals(g.user)
        return current_month_journals

    elif request.method == 'POST':
        data = request.json
        entries_obj = storage.classes.get('Entries')
        new_entry = entries_obj(user_id=g.user.id, entry=data['entry'])
        storage.add(new_entry)
        storage.save()
        latest_entry = storage.all_user_entries(g.user.id)
        latest_entry_dict = list(latest_entry.values())[0]
        storage.close()
        return latest_entry_dict.to_dict()

    elif request.method == 'PATCH':
        data = request.json
        entry_to_modify = list(storage.get('Entries', data['id']))[0]
        entry_to_modify.entry = data['entry']
        storage.add(entry_to_modify)
        storage.save()
        storage.close()
        return {'success': 'OK'}

    elif request.method == 'DELETE':
        data = request.json
        entry_to_delete = list(storage.get('Entries', data['id']))[0]
        storage.delete(entry_to_delete)
        storage.save()
        storage.close()
        return {'success': 'OK'}


def current_month_journals(user_obj):
    """Fetch a user's journal entries and insights for the current
    month and segment them by creation dates
    """

    current_month_entries = current_month_entries(user_obj.id)
    current_month_insights = current_month_insights(user_obj.id)
    all_month_data = current_month_entries.extend(current_month_inisghts)
    all_month_data.sort(key=lambda obj: obj.created_at)

    segmented_entries = {}
    fmt = '%A %B %d, %Y'

    for obj in all_month_data:
        pretty_date = obj.created_at.strftime(fmt)
        if pretty_date not in segmented_entries:
            segmented_entries[pretty_date] = list(obj.to_dict())
        else:
            segmented_entries[pretty_date] = \
                segmented_entries[pretty_date].append(obj.to_dict())

    return segmented_entries


def current_month_entries(user_id):
    """get all of a user's entry objects for the current month and return them
    as a list of objects"""

    all_user_entries = storage.all_user_entries(user_obj.id)
    all_entry_objs = [list(item)[0] for item in all_user_entries]

    current_date = datetime.now(tz=timezone.utc)
    interval = timedelta(
        days=current_date.day-1, hours=current_date.hour,
        minutes=current_date.minute, seconds=current_date.second,
        microseconds=current_date.microsecond-0.1
    )
    benchmark = current_date - interval
    current_month_entries = [
        obj for obj in all_entry_objs if obj.created_at > benchmark]

    return current_month_entries


def current_month_insights(user_id):
    """get all of a user's insight objects for the current month and
    return them as a list of objects"""

    all_user_insights = storage.all_user_insights(user_obj.id)
    all_insight_objs = [list(item)[0] for item in all_user_insights]

    current_date = datetime.now(tz=timezone.utc)
    interval = timedelta(
        days=current_date.day-1, hours=current_date.hour,
        minutes=current_date.minute, seconds=current_date.second,
        microseconds=current_date.microsecond-0.1
    )
    benchmark = current_date - interval
    current_month_insights = [obj for obj in all_insight_objs
                              if obj.created_at > benchmark]
