from datetime import datetime

from icalendar import Calendar, Event

from registrar import get_schedule

username = input("enter username:")
password = input("enter password:")
schedule = get_schedule(username, password)

cal = Calendar()
for k, day in schedule.items():
    for cl in day:
        start = datetime.strptime(cl['start_time'], "%I:%M %p").replace(year=2020, month=1, day=12)
        end = datetime.strptime(cl['end_time'], "%I:%M %p").replace(year=2020, month=1, day=12)
        ev = Event()
        ev.add('summary', cl['course_name'])
        ev.add('dtstart', start)
        ev.add('dtend', end)
        ev.add('description', cl['lecture_room'])
        ev.add('rrule', {'freq': 'weekly', 'byday': k[0:2], 'until': datetime(year=2020, month=4, day=24)})
        cal.add_component(ev)

with open("schedule.ical", "wb") as file:
    file.write(cal.to_ical())
