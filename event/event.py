from datetime import datetime

from helpers.helpers import uuid


class Event:
    def __init__(self, name, start_time, duration, location, owner, participants):
        self.id = uuid()
        self._name = name
        self._start_time = datetime.strptime(start_time, "%d/%m/%y %H:%M")
        self._duration = duration
        self._location = location
        self.owner = owner
        self._participants = participants
        self.created = datetime.now()

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, val):
        try:
            int(val)
        except ValueError:
            print('Duration must be a number')
        else:
            if int(val) < 5:
                print(f"Meeting duration under 5 minutes doesn't make sense ({val}).")
            else:
                self._duration = int(val)

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

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, new_start_time):
        try:
            self._start_time = datetime.strptime(new_start_time, "%d/%m/%y %H:%M")
        except ValueError:
            print('Wrong data format')

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        self._location = new_location

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, new_participants):
        self._participants = new_participants

    def __str__(self):
        return f'class Event(id: {self.id}, name: {self.name}, start_time: {self.start_time}, ' \
               f'created: {self.created}, {self.time_to_event}, duration: {self.duration}, location: {self.location})'
