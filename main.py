from io import StringIO

from words.custom_exceptions import GameOver
from words.data_reader import CSVGetter, APIGetter
from words.game_process import GameProcess


def play():
    data_reader = CSVGetter('words/words.csv')
    # data_reader = APIGetter()
    game = GameProcess(data_reader)
    game.play()


if __name__ == '__main__':
    while True:
        try:
            play()
        except GameOver as err:
            print(f'You completed {err.score} words')
            y = input('Enter: Y if you want to try again')
            if y.lower() != 'y':
                break
