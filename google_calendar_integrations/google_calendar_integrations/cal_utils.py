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


def get_today_timerange():
    today_start = datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0)
    today_end = today_start + datetime.timedelta(days=1, seconds=-1)

    # format the times for the API
    today_start = today_start.astimezone().isoformat()
    today_end = today_end.astimezone().isoformat()

    return today_start, today_end


def is_all_day(event):
    return (event['start'].minute == event['start'].hour == 0) and (
        event['end'].minute == event['end'].hour == 0)


def get_summary_if_possible(event):
    try:
        return event['summary']
    except KeyError:
        return "No Summary"
