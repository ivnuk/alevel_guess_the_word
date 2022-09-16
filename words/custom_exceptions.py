class GameOver(Exception):
    def __init__(self, score):
        self.score = score


class WordCompleted(Exception):
    pass


class GameCompleted(Exception):
    pass
