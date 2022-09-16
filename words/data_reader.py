import random

from words.custom_exceptions import GameCompleted


class CSVGetter:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_random_word(self, completed_words=None):
        word = ''
        if completed_words is None:
            completed_words = []
        with open(self.file_path) as fp:
            words = fp.read().split('\n')[1:]
            words_in_db = len(words)
            if len(completed_words) >= words_in_db:
                raise GameCompleted
            while not word or word in completed_words:
                word = random.choice(words)
            return word


class APIGetter:
    def get_random_word(self):
        pass
