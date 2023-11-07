#!/usr/bin/env python3
"""Implement the all_insights view, where a user sees all
their insights so far"""

from flask import g, Blueprint, redirect, url_for
from .utilities import storage

all_insights_handler = Blueprint('all_insights_view', __name__)

@all_insights_handler.route('/<username>/all-insights')

def all_insights(username):
    """Handle the all-insights view of the application where users can
       see all their insights so far
    """
    if not g.user:
        return redirect(url_for('login'))

    all_user_insights = storage.all_user_insights(g.user.id)
    all_insight_objs = [list(obj)[0] for obj in all_user_insightss]

    all_insight_objs.sort(key=lambda obj: obj.created_at)
    segmented = segment_insightss(all_insight_objs)
    return segmented


def segment_insights(insight_objs):
    """Segment a list of insight objects into a dict structure of the form:
    {
        'Year': {
            'Month': [{insight object as dict},
            {insight object as dict} ...]
        }
    }"""

    segmented = {}

    for obj in insight_objs:
        year = obj.created_at.year
        month = obj.created_at.strftime('%B')
        if not year in segmented:
            segmented[year] = {}
            segmented[year][month] = []
            segmented[year][month].append(obj.to_dict())
        else:
            if not month in segmented[year]:
                segmented[year][month] = []
                segmented[year][month].append(obj.to_dict())
            else:
                segmented[year][month].append(obj.to_dict())

    return segmented