import sys
import caldav
from datetime import datetime, timedelta

URL=""
user=""
passwd=""

def print_events(calendar):
    for event in calendar.events():
        ical_text = event.data
        print(ical_text)

def add_event(calendar,summary, start, end):

    calendar.save_event(
        dtstart=start,
        dtend=end,
        summary=summary)

def connect():
    client = caldav.DAVClient(url=URL, username=user, password=passwd)

    principal = client.principal()
    calendars = principal.calendars()
    return calendars[0]


def main():
    if len(sys.argv) != 3:
        print("Error number of parameters: summary and start date needed")
        exit(1)

    event_summary = sys.argv[1] #'Prueba molonchi'
    event_start = datetime.strptime(sys.argv[2],'%Y-%m-%d %H:%M') #datetime.now()
    event_end = event_start + timedelta(hours=1)
    personal_calendar = connect()
    add_event(personal_calendar, event_summary, event_start, event_end)

if __name__ == "__main__":
    main()
