# TODO NGY Typo
# TODO NGY Must be coherent with class diagram
class RessourceNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)