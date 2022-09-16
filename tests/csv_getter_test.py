import builtins
from io import StringIO
from unittest import TestCase
from unittest.mock import patch, mock_open

from words.data_reader import CSVGetter

READ_DATA = 'word1\nword2\nword3\n'


def get_rand(*args):
    return 'abc'


def fake_words():
    return StringIO(
        'word1\nword2\nword3\n'
    )


class CSVGetterTestCase(TestCase):

    def setUp(self) -> None:
        print('before test method')

    def tearDown(self) -> None:
        print('after test method')

    def test_csv_getter_initialization(self):
        reader = CSVGetter('dummy_file')
        self.assertIsInstance(reader, CSVGetter)

    def test_csv_getter_require_parameter(self):
        with self.assertRaises(TypeError):
            reader = CSVGetter()

    @patch('builtins.open', mock_open(read_data=READ_DATA))
    def test_get_random_word(self):
        reader = CSVGetter('dummy_file')
        word = reader.get_random_word()
        self.assertIn(word, fake_words().read())

    @patch('words.data_reader.CSVGetter.get_random_word', new=get_rand)
    def test_get_random_word_mocked(self):
        reader = CSVGetter('dummy_file')
        word = reader.get_random_word()  # get_rand()
        self.assertEqual(word, 'abc')



