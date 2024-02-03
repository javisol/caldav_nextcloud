import sys
import os
import caldav
from datetime import datetime, timedelta
import locale

def print_events(calendar):
    for event in calendar.events():
        ical_text = event.data
        print(ical_text)

def add_event(calendar,summary, start, end):

    calendar.save_event(
        dtstart=start,
        dtend=end,
        summary=summary)

def connect(url, user, password):
    client = caldav.DAVClient(url=url, username=user, password=password)

    principal = client.principal()
    calendars = principal.calendars()
    return calendars[0]

def parse_date(date):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    PATTERN = "%d de %B de %Y a las %H:%M"
    return datetime.strptime(date,PATTERN)


def main():
    url=os.environ.get("CAL_URL")
    user=os.environ.get("CAL_USER")
    password=os.environ.get("CAL_PASS")

    if not (url and user and password):
        print("CAL_URL, CAL_USER and CAL_PASS env vars must be set")
        exit(1)

    if len(sys.argv) != 3:
        print("Error number of parameters: summary and start date needed")
        exit(1)

    event_summary = sys.argv[1] #'event summary text'
    event_start = parse_date(sys.argv[2]) #datetime.now()
    event_end = event_start + timedelta(hours=1)
    personal_calendar = connect(url, user, password)
    add_event(personal_calendar, event_summary, event_start, event_end)

if __name__ == "__main__":
    main()
