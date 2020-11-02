from random import randint

from event import Event
from user import User

user = User('Pat', 'pat@gmail.com')

print(user)

event = Event('meeting', '5/11/21 15:00', 30, '', '', '')
print(event)

events = []
for x in range(0, 50):
    x = Event(f'pizza {x}', f'{randint(1, 25)}/{randint(1, 11)}/21 {randint(1, 23)}:38', randint(5, 60), '', '', '')
    events.append(x)

for event in events:
    print(event)
