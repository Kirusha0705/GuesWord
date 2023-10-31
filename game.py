import random
from colorama import init, Fore
from colorama import Back
from termcolor import colored

init(autoreset=True)

letter_up = [(lambda c: chr(c))(i) for i in range(1040, 1072)]  # Получить русский алфавит заглавных букв [list]
letters = (' '.join(letter_up))  # получить строку разделенную пробелами

words = []  # Пустой список, который мы заполним словами из файла.


def get_word():
    with open('words_for_game', encoding='utf-8') as file:
        for i in file:  # для каждого слова в файле.
            words.append(i.strip())  # Добавить слово удалив лишние символы
        guess = list(random.choice(words))  # получить из списка слов рандомное слово
        return guess


# print(random.choice(words))
# print(letters)


def start_game():
    guess = get_word()
    init(autoreset=True)
    print()
    print()
    print()
    print('---------------------------')
    print(' Угадай слово за 6 попыток ')
    print('---------------------------')
    print(f'{colored("[Угадал букву и место в слове]", "white", "on_yellow")}')
    print(f'{colored("[Такой буквы нет]", "white", "on_black")}')
    print(f'{colored("[Угадал букву]", "black", "on_white")}')

    your_words = []  # в этот список будут добавлены (а затем и распечатаны) слова игрока
    attempt = 6
    while attempt != 0:
        print('---------------------------')
        for i in letter_up:
            print(i, end=' ')
        print()
        print()

        print(f'Осталось попыток {attempt}')
        for i in your_words:
            print(' '.join(i))
        choise = list(input(f'Слово? ').upper())
        your_words.append(choise)
        print('---------------------------')

        if len(choise) != 5:
            print(colored('Введите слово из 5 букв! ', 'red', 'on_black'))
        # elif (''.join(choise)).upper() not in words:
        #     print(colored(f'Такого слова нет в нашем списке', 'red', 'on_black'))
        else:
            if choise == guess:
                print(f'Верно, вы угадали!!!')
                print(f'Загаданное слово было: {"".join(guess)}')
                break

        for lst in your_words:  # Для каждого списка в моем списке добавленных слов
            for letter in lst:  # Для каждоый буквы из списка
                if letter in guess:  # Если бува есть в загаданном слове то,
                    if lst.index(letter) != guess.index(letter):
                        dex = lst.index(letter)
                        lst.remove(letter)
                        ac = colored(letter, 'black', 'on_white')
                        lst.insert(dex, ac)
                        if letter in letter_up:
                            dex = letter_up.index(letter)
                            letter_up.remove(letter)
                            letter_up.insert(dex, ac)
                    elif lst.index(letter) == guess.index(
                            letter):  # Если индекс буквы равен индексу в загаданном слове то:
                        dex = lst.index(letter)  # Присваиваем индекс переменной
                        lst.remove(letter)  # Удаляем букву из этого слова
                        ac = colored(letter, 'black', 'on_yellow')  # Закрашиваем удаленную букву
                        lst.insert(dex, ac)  # Вставляем на удаленный индекс, закрашенную букву
                        if letter in letter_up:
                            dex = letter_up.index(letter)
                            letter_up.remove(letter)
                            letter_up.insert(dex, ac)
                else:
                    dex = lst.index(letter)
                    lst.remove(letter)
                    ac = colored(letter, 'white', 'on_black')
                    lst.insert(dex, ac)
                    if letter in letter_up:
                        dex = letter_up.index(letter)
                        letter_up.remove(letter)
                        letter_up.insert(dex, ac)

        attempt -= 1


    else:
        print(f'К сожалению вы не смогли отгадать')
        print(f'Загаданное слово было: {" ".join(guess)}')


while True:
    start_game()
    print('-----------------------------------')
    input('Нажмите enter, чтобы начать заного')

    letter_up = [(lambda c: chr(c))(i) for i in range(1040, 1072)]
