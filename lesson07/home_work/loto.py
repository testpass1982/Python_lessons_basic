#!/usr/bin/python3
import random
import time
"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


class Player(object):
    def __init__(self):
        self.card=Card()
        self.points = 0

    def mark(self, barrel=None):
        if self.cardCheck(barrel):
            time.sleep(2)
            print('You got it! Now it\'s computer\'s turn!')
            self.points+=1
            self.card.update(barrel)
        else:
            print('You made a mistake! Game over! You lose!')
            Quit.confirm=True

    def next(self, barrel=None):
        if self.cardCheck(barrel)==True:
            time.sleep(2)
            print ('...but it is in your card! You lose!')
            Quit.confirm=True
        else:
            pass

    def cardCheck(self, barrel):
        cm = self.card.getCard()
        for row in cm:
            for el in row:
                if el == barrel:
                    return True
        return False


class Human(Player):
    def __init__(self):
        super().__init__()
        print ('Hello, human!')
        print ('Here is your card, human!')
        time.sleep(2)
        self.card.makeNewCard()

    def makeTurn(self, barrel=None):
        #выбрать вариант хода: зачеркнуть цифру? (y/n), продолжить (n)
        #выйти из игры (q)
        print('------- Your card ----------')
        self.card.drawCard()
        time.sleep(2)
        print('We pull a keg: ', barrel)
        time.sleep(2)
        print('''Make a choice for your turn:
- "y" for cross the number in your card, 
- "n" for next turn, 
- "q" for quit''')

        turn = input("Your choice -> ")
        if turn == 'y':
            print('You decide to stike out the number')
            self.mark(barrel)
        if turn == 'n':
            print('You decide to pull another keg...')
            self.next(barrel)
        if turn == 'q':
            print('''
  ________                __                           ____                    __            _             __
 /_  __/ /_  ____ _____  / /__   __  ______  __  __   / ______  _____   ____  / ____ ___  __(_____  ____ _/ /
  / / / __ \/ __ `/ __ \/ //_/  / / / / __ \/ / / /  / /_/ __ \/ ___/  / __ \/ / __ `/ / / / / __ \/ __ `/ / 
 / / / / / / /_/ / / / / ,<    / /_/ / /_/ / /_/ /  / __/ /_/ / /     / /_/ / / /_/ / /_/ / / / / / /_/ /_/  
/_/ /_/ /_/\__,_/_/ /_/_/|_|   \__, /\____/\__,_/  /_/  \____/_/     / .___/_/\__,_/\__, /_/_/ /_/\__, (_)   
                              /____/                                /_/            /____/        /____/   ''')
            Quit.confirm=True
        while turn not in ('y', 'n', 'q'):
            turn = input('You have to make a choice: only \'y\', \'n\', or \'q\': ')


class Computer(Player):
     def __init__(self):
         super().__init__()
         self.card.makeNewCard()

     def makeTurn(self, barrel=None):
        print('Computer turn...')
        time.sleep(2)
        print('----- Computer\'s card ------')
        if self.cardCheck(barrel):
            self.points+=1
        self.card.update(barrel)
        self.card.drawCard()


class Card(object):
    def __init__(self):
        self.all_cards = [x for x in range(1, 91)]
        self.card_limit = 27
        self.numbers_total = 15
        self.card = self.makeNewCard()

    # создаем новую карту
    def makeNewCard(self):
        c = 0
        self.random_numbers = random.sample(self.all_cards, self.numbers_total)
        self.card = [[' ' for x in range(9)] for e in range(3)]
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                if j <= 4:
                    self.card[i][j]=self.random_numbers[c]
                    c+=1
        for i in range(len(self.card)):
            random.shuffle(self.card[i])
        return self.card

    # тут мы храним текущее состояние карты с изменениями
    def getCard(self, barrel=None):
        self.c = self.card[:]
        if self.update(barrel):
            self.c = self.update(barrel)
        return self.c

    # печатаем карту
    def drawCard(self):
        for i in self.getCard():
            print(' '.join(map(str, i)))
        print('-----------------------------')

    # обновляем карту в соответствии с бочонком
    def update(self, barrel):
        for row in self.card:
            for el in range(len(row)):
                if row[el] == barrel:
                    row[el] = 'X'
        return self.card
    
class Bag(object):
    def __init__(self):
        self.reserve = [x for x in range (1, 91)]

    # тащим из сумки бочонок
    def pull(self):
        barrel = random.choice(self.reserve)
        self.reserve.remove(barrel)
        return barrel

class Quit(object):
    def __init__(self, choice):
        self.choice = choice
    
    @property
    def confirm(self):
        if self.choice == 'y':
            return False
        if self.choice == 'n':
            return True
    

if __name__ == '__main__':
    print ("""    ___________          __   ____ __________     ____________  _______________
   /  _/_  __( )_____   / /  / __ /_  __/ __ \   /_  __/  _/  |/  / ____/ / / /
   / /  / /  |// ___/  / /  / / / // / / / / /    / /  / // /|_/ / __/ / / / / 
 _/ /  / /    (__  )  / /__/ /_/ // / / /_/ /    / / _/ // /  / / /___/_/_/_/  
/___/ /_/    /____/  /_____\____//_/  \____/    /_/ /___/_/  /_/_____(_(_(_)   
                                                                               
Here are the rules for our game:
1 we give you cards
2 we pull a keg from bag and you check if keg is in your card
3 the winner has the maximum points
Enjoy our game!
----------------------------""")
    choice = input('Start new game? (y/n) : ')
    while choice not in ('y', 'n'):
        choice = input('Please, input \'y\' or \'no\': ')

    done = Quit(choice)
    bag = Bag()
    if not done.confirm:
        player = Human()
        computer = Computer()
    while done.confirm==False:
        keg = bag.pull()
        player.makeTurn(keg)
        if not done.confirm:
            computer.makeTurn(keg)
        time.sleep(1)
        print('Your points: ', player.points)
        time.sleep(1)
        print('Computer points: ', computer.points)
        time.sleep(1)
        if player.points == 15:
            print('Player wins!')
        elif computer.points == 15:
            print('Computer wins!')