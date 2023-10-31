#!/usr/bin/env python3
"""Implement the journal area, where a user sees their entries for the last
       30 days and can make new entries"""
from flask import request, g, Blueprint, redirect, url_for
from . import storage

journal_area_view = Blueprint('journal_area_view', __name__)

@journal_area_view.route('/<username>/entries',
                         methods=['GET', 'POST', 'PATCH', 'DELETE'])
def journal_area(username):
    """Handle the main chat area view of the application where users can
       can see their entries for the last 30 days and make new ones
    """
    if not g.user:
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        last_30day_journals = last_30day_journals(g.user)
        return last_30day_journals
    
    elif request.method == 'POST':
        data = request.json
        entries_obj = storage.classes.get('Entries')
        new_entry = entries_obj(user_id=g.user.id, entry=data['entry'])
        storage.add(new_entry)
        storage.save()
        latest_entry = storage.all_user_entries(g.user.id)
        latest_entry_dict = list(latest_entry.values())[0]
        storage.close()
        return latest_entry_dict
    
    elif request.method == 'PATCH':
        data = request.json
        entry_to_modify = list(storage.get('Entries', data['id']))[0]
        entry_to_modify.entry = data['entry']
        storage.add(entry_to_modify)
        storage.save()
        storage.close()

    elif request.method == 'DELETE':
        data = request.json
        entry_to_delete = list(storage.get('Entries', data['id']))[0]
        storage.delete(entry_to_delete)
        storage.close()


def last_30day_journals(user_obj):
    """Fetch a user's journal entries for the last 30 days and segment
       them by entry dates
    """
    all_user_entries = storage.all_user_entries(user_obj.id)
    all_entry_objs = [list(item)[0] for item in all_user_entries]

    segmented_entries = {}
    fmt = '%A, %b. %d'
    
    for obj in all_entry_objs:
        pretty_date = obj.created_at.strftime(fmt)
        if pretty_date not in segmented_entries:
            segmented_entries[pretty_date] = list(obj.to_dict())
        else:
            segmented_entries[pretty_date] = \
                segmented_entries[pretty_date].append(obj.to_dict())

    return segmented_entries
