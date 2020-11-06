from random import randint

from event import Event
from events import Events
from user import User

user = User('Pat', 'pat@gmail.com')

events = Events()
for x in range(50):
    event = Event(f'pizza {x}', f'{randint(1, 25)}/{randint(1, 11)}/21 {randint(1, 23)}:38', randint(5, 60), '', '', '')
    events.add_event(event)

# for event in events.get_events():
#    print(event)

# print(events.get_event(3))

# print(events.delete_event(3))
events.update_event(3, {'name': 'yolo'})
events.update_event(3, {'duration': 22})
# TODO add support for multiple updates (zeby zmodyfikowac kilka na raz, jeden slownik w ktorym jest wiele par key:val)
# print(events.get_event(3))

events.sort_config = []
for event in events.sort_event():
    print(event)