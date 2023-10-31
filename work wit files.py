from colorama import init, Fore
from colorama import Back
from colorama import Style
import random


init(autoreset=True)  #чтобы не сбрасывать настройки цвета в ручную.
"""1. Смысл этой функции в сбрасывании настроек цвета. 
Если стоит True: 2 подрят вызваные строки будут разными (одна будет с цветом, 2ая будет стандартная
2. Именно из-за этой функции у меня цвет фона на всю стоку, а не на длину слова"""


# print(Fore.BLUE + 'some red text')  #цвет текста
# print(Back.WHITE + 'and with a green background')  #Цвет фона

"""так надо каким-то образом рандом брать слово из ФАЙЛА (длина которого == 5)"""

with open('слова.txt', encoding='utf=8') as file, open('words_for_game', 'w', encoding='utf=8') as f:
    words = file.readlines()  #получим список c символом переноса строки ('\n')

    #print(f'файл имеет {len(words ):_} слов')  #после len(word) можно поставить двоеточие и символ разделения

    for i in words:
        if len(i.strip()) == 5:
                f.write(i.upper())


print()


