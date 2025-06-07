import pytest
from unittest.mock import patch
from lototron import Lototron

class TestLototron:

    def test_create_class(self):
        loto = Lototron()
        assert sorted(loto.numbers) == list(range(1, 91))
        assert loto.card_count == 0
        assert loto.human_count == 0
        assert loto.all_cards == []
        assert loto.winner == []

    @patch('builtins.input', side_effect=['3', '2'])
    def test_get_start_info(self, mock_input):
        loto = Lototron()
        assert loto.get_start_info() is True
        assert loto.card_count == '3'
        assert loto.human_count == '2'
        
    @patch('builtins.input', side_effect=['1', '2'])  # Некорректный ввод (меньше 2)
    def test_get_start_info_invalid_card_count(self, mock_input, capsys):
        loto = Lototron()
        assert loto.get_start_info() is False
        captured = capsys.readouterr()
        assert captured.out == "Минимальное кол-во участников 2\n"

    @patch('builtins.input', side_effect=['3', '4'])  # Некорректный ввод (больше общего кол-ва)
    def test_get_start_info_invalid_human_count(self, mock_input, capsys):
        loto = Lototron()
        assert loto.get_start_info() is False
        captured = capsys.readouterr()
        assert captured.out == "Число должно быть не больше общего кол-ва игроков\n"

    @patch('builtins.input', side_effect=['3', 'a'])  # Некорректный ввод (не число)
    def test_get_start_info_invalid_human_count_not_digit(self, mock_input, capsys):
        loto = Lototron()
        assert loto.get_start_info() is False
        captured = capsys.readouterr()
        assert captured.out == "Введите число\n"

    @patch('builtins.input', side_effect=['b', '2'])  # Некорректный ввод (не число)
    def test_get_start_info_invalid_card_count_not_digit(self, mock_input, capsys):
        loto = Lototron()
        assert loto.get_start_info() is False
        captured = capsys.readouterr()
        assert captured.out == "Введите число\n"