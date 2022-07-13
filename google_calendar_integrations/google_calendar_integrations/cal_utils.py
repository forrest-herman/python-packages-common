# cal_utils.py
import datetime
from dateutil import parser


def filter_events_by_calendar(events_list, calendar_names, exclude=False):
    included_events = []

    for event in events_list:
        # check XOR
        if (bool(event['calendar'] in calendar_names) != exclude):
            included_events.append(event)

    return included_events


def get_date_from_iso(iso_date):
    try:
        date = datetime.datetime.fromisoformat(iso_date)
    except ValueError:
        date = parser.isoparse(iso_date)
    return date


def get_datetime_from_event(event_time):
    try:
        return get_date_from_iso(event_time['dateTime'])
    except KeyError:
        return get_date_from_iso(event_time['date']).replace(tzinfo=datetime.timezone.utc)
