from unittest import TestCase
from unittest.mock import patch

from words.game_process import GameProcess


class FakeReader:
    def get_random_word(self):
        return 'test'


class GameProcessTestCase(TestCase):
    def setUp(self) -> None:
        self.test_reader = FakeReader()
        self.test_game = GameProcess(self.test_reader)

    def test_hidden_word(self):
        self.assertEqual(len(self.test_game.hidden_word), len(self.test_game.word))
        self.assertEqual(self.test_game.hidden_word, "****")

