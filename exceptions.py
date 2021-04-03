# Custom exceptions
class ContactExists(Exception):
    def __init__(self, name=None):
        self.message = f"Contact {name} already exists"
        super().__init__(self.message)


class ContactNotFound(Exception):
    def __init__(self, name=None):
        self.message = f"Contact {name} not found"
        super().__init__(self.message)
