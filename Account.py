from State import *

# context
class UserAccount():
    currentState = None

    def __init__(self) -> None:
        self.currentState = Online()
        # online = default, offline, busy, do no disturb, away, in a meeting

    def alert(self) -> None:
        self.currentState.alert()

    def setState(self, state) -> None:
        # print("Resetting status...")
        self.currentState = state
        self.alert()
