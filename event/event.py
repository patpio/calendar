# TODO add getters and setters
from datetime import datetime

from helpers.helpers import uuid


class Event:
    def __init__(self, name, start_time, duration, location, owner, participants):
        self.id = uuid()
        self._name = name
        self.start_time = datetime.strptime(start_time, "%d/%m/%y %H:%M")
        self._duration = duration
        self.location = location
        self.owner = owner
        self.participants = participants
        self.created = datetime.now()

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, val):
        if val < 5:
            raise ValueError(f"Meeting duration under 5 minutes doesn't make sense ({val}).")
        self._duration = val

    @property
    def time_to_event(self):
        td = self.start_time - datetime.now()
        days = td.days
        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'Time to event: {days} days, {hours} hours, {minutes} minutes.'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f'class Event(id: {self.id}, name: {self.name}, start_time: {self.start_time}, ' \
               f'created: {self.created}, {self.time_to_event}, duration: {self._duration})'
