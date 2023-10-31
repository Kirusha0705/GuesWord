import random
from colorama import init, Fore
from colorama import Back
from termcolor import colored

init(autoreset=True)

# a = ['БРОВЬ', 'ПИВКО']
# b = 'бровь'



            # a.insert(letter[0], colored(letter[1],'red'))

# print(a)
c1 = []
c = 'А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'.split()

word = [list('БРОВЬ'), list('ПИВКО')]
guess = ['Т', 'Р', 'Е', 'Б', 'А']

for lst in word:
    for letter in lst:
        if letter in guess:
            if lst.index(letter) == guess.index(letter):
                dex = lst.index(letter)
                lst.remove(letter)
                ac = colored(letter, 'black', 'on_yellow')
                lst.insert(dex, ac)
            elif lst.index(letter) != guess.index(letter):
                dex = lst.index(letter)
                lst.remove(letter)
                ac = colored(letter, 'black', 'on_white')
                lst.insert(dex, ac)
        else:
            dex = lst.index(letter)
            lst.remove(letter)
            ac = colored(letter, 'white', 'on_black')
            lst.insert(dex, ac)



for i in word:
    print(' '.join(i))

for i in c:
    if i == 'О':
        dex = c.index(i)  #узнаем индекс буквы
        c.remove(i)  #удаляем букву
        ac = colored(i, 'red')  #закрашиваем букву в нужный цвет
        c.insert(dex, colored(i, 'black', 'on_yellow'))  #вставляет на место индекса, закрашенную букву




#print(' '.join(c))


