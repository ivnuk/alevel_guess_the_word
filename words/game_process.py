from words.custom_exceptions import GameOver, WordCompleted
from words import config


class GameProcess:
    def __init__(self, data_reader):
        self.data_reader = data_reader
        self.word = self.data_reader.get_random_word().lower()
        self.used_letters = []
        self.completed_words = []
        self.tries = config.TRIES
        self.score = 0

    @property
    def hidden_word(self):
        hidden_word = []
        for letter in self.word:
            hidden_word.append(letter if letter in self.used_letters else '*')
        return ''.join(hidden_word)

    def stop_game(self):
        raise GameOver

    def validate_letter(self, letter):
        letter = letter.lower()
        if not letter.isalpha():
            print('You can enter only letters.')
            return
        if letter in self.used_letters:
            print("You've already used this letter")
            print(f"Used letters: {','.join(self.used_letters)}")
            return
        if letter in self.word:
            self.used_letters.append(letter)
            if self.hidden_word.count('*') == 0:
                print("You won!")
                raise WordCompleted
            else:
                print('congrats! Choose the next one!')
                return
        print('Wrong!')
        self.used_letters.append(letter)
        self.tries -= 1
        if self.tries == 0:
            print('Game over')
            raise GameOver(self.score)
        print(f'Tries left {self.tries}')

    def play(self):
        while True:
            print('------------------------------------------------')
            print('The word is - ', self.hidden_word)
            letter = input('Enter the letter: ')
            try:
                self.validate_letter(letter)
            except WordCompleted:
                self.score += 1
                self.completed_words.append(self.word)
                self.used_letters = []
                self.tries += 5
                self.word = self.data_reader.get_random_word(self.completed_words).lower()
