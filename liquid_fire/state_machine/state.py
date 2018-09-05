class State:
    def enter(self):
        return NotImplementedError

    def exit(self):
        return NotImplementedError

    def add_listeners(self):
        return NotImplementedError

    def remove_listeners(self):
        return NotImplementedError
