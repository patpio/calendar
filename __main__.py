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
events.update_event(49, {'name': 'elo', 'start_time': '10/11/20 15:00', 'duration': 6})
events.update_event(48, {'name': 'hi there', 'duration': 6, 'location': 'Krk'})
events.update_event(47, {'name': 'hi there', 'duration': 6, 'location': 'Krk'})

# print(events.get_event(3))

# events.sort_config = ['name']
# for event in events.sort_event():
#     print(event)

events.filter_config = {'name': 'hi there', 'duration': 6, 'location': 'Krk'}
for event in events.filter_event():
    print(event)
