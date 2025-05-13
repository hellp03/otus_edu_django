import random
from utils import clean_monitor
from card import HumanCard,RobotCard


class Lototron:
    """Класс Лототрон выполняет первичный сбор информации для игры,
       создает карты для игроков и выполняет основной процесс игры
    """

    def __init__(self):
        self.numbers = random.sample(range(1,91),90)
        self.card_count = 0
        self.human_count = 0
        self.all_cards = []
        self.winner = []

    def get_start_info(self):
        """
        Метод для сбора первоначальной информации для старта игры.
        Возвращает True если все необходимые данные собраны.
        """
        clean_monitor()
        self.card_count = input('Введите кол-во игроков (минимальное кол-во 2): ')
        clean_monitor()
        if not self.card_count.isdigit():
            print('Введите число')
            return False
        elif int(self.card_count) < 2:
            print('Минимальное кол-во участников 2')
            return False
        self.human_count = input('Введите кол-во живых игроков '
                            '(число должно быть не больше общего кол-ва игроков,'
                            'за остальных будет играть компьютер): ')
        clean_monitor()
        if not self.human_count.isdigit():
            print('Введите число')
            return False
        elif int(self.human_count) > int(self.card_count):
            print('Число должно быть не больше общего кол-ва игроков')
            return False
        return True

    def make_cards(self):
        """
        Метод создания игровых карт
        Результат выполнения - заполнение аргумента all_cards
        экземплярами классов RobotCard и HumanCard
        """
        if int(self.human_count) > 0:
            gamers = [input(f'Введите имя игрока-{i}: ') for i in range(int(self.human_count))]
            HumanCards = [HumanCard(i) for i in gamers]
            self.all_cards += HumanCards
        if int(self.card_count) - int(self.human_count) > 0:
            RobotCards = [RobotCard('Computer-' + str(i)) for i in range(int(self.card_count) - int(self.human_count))]
            self.all_cards += RobotCards

    def start_game(self):
        """
        Метод описывает игровой процесс используя первоначальные данные
        полученные от пользователя и сгенерированные игровые карты
        Результат выполнения - заполнение аргумента winner именами победителей
        """
        get_winner = False
        for num in self.numbers:
            for card in self.all_cards:
                clean_monitor()
                print('Номер - ', num)
                card.print_card()
                if not card.check_number(num):
                    return False
                if card.check_win():
                    get_winner = True
                    self.winner.append(card.name)
            if get_winner:
                return True