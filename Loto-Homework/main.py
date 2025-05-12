
import random
import os
from abc import ABC, abstractmethod

class Lototron:
    def __init__(self):
        self.numbers = random.sample(range(1,91),90)
class Utils:
    def clean_monitor(self):
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

class Card(ABC):
    def __init__(self,name=''):
        self.card = self._get_card()
        self.name = name

    def _get_card(self):
        m = random.sample(range(1, 91), 15)
        m3x5=[m[:5],m[5:10],m[10:]]
        return self._sort(m3x5)

    def _sort(self, m):
        for i in m:
            i.sort()
        return m

    @abstractmethod
    def check_number(self, number):
        pass

    def check_win(self):
        if sum(self.card[0]) + sum(self.card[1]) + sum(self.card[2]) == 0:
            return True
        else:
            return False

    def print_card(self):
        print('-'*6,self.name,'-'*6)
        for i in self.card:
            for j,k  in enumerate(i):
                if j==4: e='\n'
                else: e='\t'
                if k==0: print ('-', end=e)
                else: print(k,end=e)
        print('-' * 25)


class Robot_Card(Card):
    def check_number(self, number):
        for i in self.card:
            if number in i:
                i[i.index(number)] = 0
                break
        return True

class Human_Card(Card):

    def check_number(self, number):
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

utils=Utils()
all_info_was_get=False
while not all_info_was_get:
    utils.clean_monitor()
    card_count=input('Введите кол-во игроков (минимальное кол-во 2): ')
    utils.clean_monitor()
    if not card_count.isdigit():
        print('Введите число')
        continue
    elif int(card_count)<2:
        print('Минимальное кол-во участников 2')
        continue
    human_count=input('Введите кол-во живых игроков '
                      '(число должно быть не больше общего кол-ва игроков,' 
                      'за остальных будет играть компьютер): ')
    utils.clean_monitor()
    if not human_count.isdigit():
        print('Введите число')
        continue
    elif int(human_count)>int(card_count):
        print('Число должно быть не больше общего кол-ва игроков')
        continue
    all_info_was_get=True
all_cards=[]
if int(human_count)>0:
    gamers=[input(f'Введите имя игрока-{i}: ') for i in range(int(human_count))]
    human_cards=[Human_Card(i) for i in gamers]
    all_cards+=human_cards
if int(card_count)-int(human_count)>0:
    robot_cards = [Robot_Card('Computer-'+str(i)) for i in range(int(card_count)-int(human_count))]
    all_cards +=robot_cards

loto=Lototron()
get_winner=False
winner=[]
for num in loto.numbers:
    for card in all_cards:
        utils.clean_monitor()
        print('Номер - ', num)
        card.print_card()
        if not card.check_number(num):
            quit()
        if card.check_win():
            get_winner=True
            winner.append(card.name)
    if get_winner: break
for i in winner:
    print(i, ' - Win!')