# interface
class ISocialMediaStatus:
    def alert(): pass

# states
class Online(ISocialMediaStatus):
    # singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Online, cls).__new__(cls)
        return cls.instance

    def alert(self) -> None:
        print("Status set to Online...")

class Offline(ISocialMediaStatus):
    # singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Offline, cls).__new__(cls)
        return cls.instance

    def alert(self) -> None:
        print("Status set to Offline...")

class Busy(ISocialMediaStatus):
    # singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Busy, cls).__new__(cls)
        return cls.instance

    def alert(self) -> None:
        print("Status set to Busy...")

class DnD(ISocialMediaStatus):
    # singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DnD, cls).__new__(cls)
        return cls.instance

    def alert(self) -> None:
        print("Status set to Do not disturb...")

class Away(ISocialMediaStatus):
    # singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Away, cls).__new__(cls)
        return cls.instance

    def alert(self) -> None:
        print("Status set to Away...")

class Meeting(ISocialMediaStatus):
    # singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Meeting, cls).__new__(cls)
        return cls.instance

    def alert(self) -> None:
        print("Status set to In a meeting...")