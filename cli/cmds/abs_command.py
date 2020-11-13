from abc import ABC, abstractmethod

from events import Events


class AbsCommand(ABC):
    events = Events()

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self):
        pass
