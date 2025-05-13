from abc import ABC, abstractmethod
import random

class Card(ABC):
    """
    Абстрактный класс описывающий методы создания карты,
    проверки победителя и отрисовки карты
    """
    def __init__(self,name=''):
        self.card = self._get_card()
        self.name = name

    def _get_card(self):
        """Метод создания карты (массива 3 на 5 заполненными рандомными числами от 1 до 90)."""
        m = random.sample(range(1, 91), 15)
        m3x5=[m[:5],m[5:10],m[10:]]
        return self._sort(m3x5)

    def _sort(self, m):
        """Вспомогательный метод для сортировки чисел в карте."""
        for i in m:
            i.sort()
        return m

    @abstractmethod
    def check_number(self, number):
        pass

    def check_win(self):
        """Метод определяет победителя (когда все числа в карте вычеркнуты (равны 0))."""
        if sum(self.card[0]) + sum(self.card[1]) + sum(self.card[2]) == 0:
            return True
        else:
            return False

    def print_card(self):
        """Метод отображения карты на экране"""
        print('-'*6,self.name,'-'*6)
        for i in self.card:
            for j,k  in enumerate(i):
                if j==4: e='\n'
                else: e='\t'
                if k==0: print ('-', end=e)
                else: print(k,end=e)
        print('-' * 25)

class RobotCard(Card):
    """Дочерний класс для работы с картами компьютера."""
    def check_number(self, number):
        """
        Метод проверки нахождения числа в карте компьютера
        При нахождении числа в карте число в карте обнуляется
        """
        for i in self.card:
            if number in i:
                i[i.index(number)] = 0
                break
        return True

class HumanCard(Card):
    """Дочерний класс для работы с картами компьютера."""
    def check_number(self, number):
        """
        Метод проверки нахождения числа в карте человека
        При нахождении числа в карте число в карте обнуляется
        Но если человек не правильно отвечает на вопрос, присутствует
        ли число в его карте, игра заканчивается.
        """
        for i in self.card:
            if number in i:
                i[i.index(number)] = 0
                number_in_card=True
                break
        else:
            number_in_card=False
        print('Зачеркнуть цифру? (y/n)')
        while True:
            answer=input()
            if answer=='y' or answer=='n':
                break
            else: print("Введите y или n")
        if (answer=='y' and not number_in_card) or (answer=='n' and number_in_card):
            print(self.name, ' - вы проиграли! \nИгра окончена')
            return False
        return True

