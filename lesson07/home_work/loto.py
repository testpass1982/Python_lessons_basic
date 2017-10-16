#!/usr/bin/python3
import random
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
        self.points = 90
        print('The game started')
        self.card=Card()

    def makeTurn(self):
        #выбрать вариант хода: зачеркнуть цифру? (y/n), продолжить (n)
        #выйти из игры (q)
        print('''Make a choice for your turn:
- "y" for cross the number in your card, 
- "n" for next turn, 
- "q" for quit
        ''')
        turn = input("Your choice: ")
        if turn == 'y':
            print('you cross the number')
            self.updateCard()
        if turn == 'n':
            print('now we pull another keg')
        if turn == 'q':
            print('thank you for playing!')
            Quit.confirm=True
        if turn not in ('y', 'n', 'q'):
            print ('!!! you have to make a choice: only "y", "n", or "q" !!!')

    def updateCard(self):
        pass

class Human(Player):
    def __init__(self):
        super().__init__()
        print ('Hello, human!')
        print ('Here is your card, human!')
        print (self.card.makeNewCard())

class Computer(Player):
     pass

class Card(object):
    def __init__(self):
        self.all_cards = [x for x in range(1, 91)]
        self.card_limit = 27
        self.numbers_total = 15

    def makeNewCard(self):
        self.random_numbers = random.sample(self.all_cards, self.numbers_total)
        self.card = [['' for x in range(0, 9)] for e in range(3)]

        return self.blank_card

    def getCard(self):
        pass

    def drawCard(self):
        print('------ Ваша карточка -----')
        print(self.getCard())
        print('--------------------------')
    
class Bag(object):
    def __init__(self):
        self.reserve = [x for x in range (1, 91)]
        
    def remove_from_bag(self, number):
        reserve.remove(number)

class Keg(object):
    pass

class Quit(object):
    def __init__(self, choice):
        self.choice = choice
    
    @property
    def confirm(self):
        if self.choice == 'yes':
            return False
        if self.choice == 'no':
            return True
    

if __name__ == '__main__':
    print ("""These are rules of our game:
1 rule
2 rule
Enjoy our game!
----------------------------""")
    
    bag = Bag()
    choice = input('Start new game? (yes/no) : ')
    done = Quit(choice)
    if not done.confirm:
        player = Human()
    while not done.confirm:
        
        player.makeTurn()
        
    print ('Goodbye!')
    

        
            
            
