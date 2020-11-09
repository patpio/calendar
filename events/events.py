from filtering import Filter
from sorting import Sort


class Events:
    def __init__(self):
        self._events = []
        self.sort_config = []
        self.filter_config = {}

    def add_event(self, event):
        self._events.append(event)

    @Sort.sort
    @Filter.filter
    def get_events(self):
        return self._events

    def get_event(self, idx):
        result = list(filter(lambda x: x.id == idx, self._events))
        try:
            return result[0]
        except IndexError:
            return False

    def delete_event(self, idx):
        event = self.get_event(idx)
        if event:
            self._events.remove(event)
            return True
        return False

    def update_event(self, idx, config):
        event = self.get_event(idx)
        if event:
            # key = list(config.keys())[0]
            keys = [*config]  # *config - pobiera wszystkie klucze ze slownika # notepad https://www.sublimetext.com/3
            for key in keys:
                setattr(event, key, config[key])

    # @Sort.sort
    # def sort_event(self):
    #     return self._events
    #
    # @Filter.filter
    # def filter_event(self):
    #     return self._events
