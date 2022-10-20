"""поле чудес."""
import random
import time


def get_question():
    """получить вопрос-ответ."""
    with open('question.txt', 'r', encoding='utf-8') as file:
        q_list = file.read().splitlines()
    number_q = random.randrange(0, len(q_list))
    q_answer = str(q_list[number_q])
    for i, ans in enumerate(q_answer):
        if ans == ';':
            question = q_answer[0:i]
            answer = q_answer[i + 1:len(q_answer)].lower()
    return answer, question


def encrypt(answer):
    """шифровать."""
    curent_view = []
    for i in range(len(answer)):
        curent_view.append('*')
    return curent_view


def guess_letter(answer, curent_view, letter):
    """угадать букву."""
    if letter in answer:
        print('Такая буква есть!')
        for i, ans in encrypt(answer):
            if ans == letter:
                curent_view[i] = letter
    else:
        print('Такой буквы нет')
    print("слово: " + "".join(curent_view) + "\n")
    return curent_view


def guess_word(answer, word):
    """угадать слово."""
    if answer == word:
        return True
    return False


def drum(score):
    """барабан."""
    drum_list = [100, 200, 300, 400, 500, 600, 1000, 'Банкрот']
    value = drum_list[random.randrange(0, len(drum_list))]
    if value == 'Банкрот':
        print('Вам выпал банкрот, ваш счет обнулился\n')
        return 0
    print('Вам выпало ' + str(value) +
          '. Ваш счет: ' + str(score + value) + '\n')
    return score + value


def compare(curent_view):
    """проверка."""
    for i in enumerate(curent_view):
        if curent_view[i] == '*':
            return False
    return True


def check_letter(letter):
    """проверка буквы."""
    rus_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й",
                   "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
                   "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    if letter in rus_letters:
        return True
    return False


def main():
    """главная функция."""
    answer, question = get_question()
    score = 0
    curent_view = encrypt(answer)
    win = False
    print(question + '? ' + "".join(curent_view) + '\n')
    while True:
        print('Вращайте барабан')
        time.sleep(2)
        score = drum(score)
        tem = input('Вы готовы назвать слово? ').lower()
        if tem == 'да':
            word = input('Ввыедите слово ').lower()
            if guess_word(answer, word):
                win = True
            else:
                print('\nНеверно. Вы проиграли, ваш счет: ' + str(score))
                break
        else:
            letter = ''
            while not check_letter(letter):
                letter = input('Введите букву ').lower()
            curent_view = guess_letter(answer, curent_view, letter)
            if compare(curent_view):
                win = True
            time.sleep(2)
        if win:
            print('Вы победили со счетом: ' + str(score))
            break


main()
