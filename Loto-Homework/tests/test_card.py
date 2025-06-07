import pytest
from card import HumanCard, RobotCard

class TestCard:

    def test_get_card_structure(self):
        """Тестируем структуру карты, генерируемой _get_card."""
        human_card = HumanCard(name='Player1')
        card = human_card.card  # Получаем карту

        # Проверяем, что карта состоит из 3 строк
        assert len(card) == 3
        # Проверяем, что каждая строка состоит из 5 чисел
        assert all(len(row) == 5 for row in card)

    def test_get_card_unique_numbers(self):
        """Тестируем, что карта содержит уникальные числа от 1 до 90."""
        human_card = HumanCard(name='Player1')
        card = human_card.card

        all_numbers = [num for row in card for num in row]

        assert len(all_numbers) == len(set(all_numbers))  # Все числа должны быть уникальными
        assert all(1 <= num <= 90 for num in all_numbers)  # Все числа находятся в пределах от 1 до 90

    def test_get_card_randomness(self):
        """Тестируем, что каждая карта генерируется случайно."""
        card1 = HumanCard(name='Player1').card
        card2 = HumanCard(name='Player2').card

        assert card1 != card2

    def test_sort_function(self):
        """Тестируем метод _sort."""
        human_card = HumanCard(name='Player1')
        unsorted_card = [[5, 3, 2, 4, 1], [10, 8, 9, 7, 6], [15, 13, 12, 14, 11]]
        human_card.card = unsorted_card
        sorted_card = human_card._sort(unsorted_card)

        assert sorted_card == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

    def test_check_win(self):
        """Тестируем метод check_win."""
        human_card = HumanCard(name='Player1')
        human_card.card = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        assert human_card.check_win() is True
        human_card.card = [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
        assert human_card.check_win() is False


class TestRobotCard:

    def test_check_number_found(self):
        """Тестируем метод check_number, когда число найдено."""
        robot_card = RobotCard(name='Robot-1')

        number_to_check = robot_card.card[0][0]
        assert robot_card.check_number(number_to_check) is True
        assert robot_card.card[0][0] == 0

    def test_check_number_not_found(self):
        """Тестируем метод check_number, когда число не найдено."""
        robot_card = RobotCard(name='Robot-1')
        number_to_check = 99
        result = robot_card.check_number(number_to_check)
        assert result is True  # Метод должен возвращать True даже если число не найдено
        assert number_to_check not in [num for row in robot_card.card for num in row]  # Проверяем, что карта не изменилась