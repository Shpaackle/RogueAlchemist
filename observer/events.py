from typing import List

from .publisher import Publisher


class Event:
    def __init__(self, name):
        self.name = name


class EventHandler(Publisher):
    def __init__(self, events: List[Event]):
        super().__init__(events)

    def get_subscribers(self, event: Event) -> dict:
        return super().get_subscribers(event)

    def register(self, event: Event, who, callback=None):
        super().register(event, who, callback)

    def unregister(self, event: Event, who):
        super().unregister(event, who)

    def dispatch(self, event: Event, message):
        super().dispatch(event, message)
