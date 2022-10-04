import random
import time


def get_question(number_q):
    with open('question.txt', 'r', encoding='utf-8') as f:
        q_list = f.read().splitlines()
    q_answer = str(q_list[number_q])
    for i in range(0, len(q_answer)):
        if q_answer[i] == ';':
            question = q_answer[0:i]
            answer = q_answer[i + 1:len(q_answer)].lower()
    return answer, question

def encrypt(answer):
    curent_view = []
    for i in range(0, len(answer)):
        curent_view.append('*')
    return curent_view

def guess_letter(answer, curent_view, letter):
    if letter in answer:
        for i in range(0, len(answer)):
            if answer[i] == letter:
                curent_view[i] = letter
    return curent_view

def guess_word(answer, word):
    if answer == word:
        return True
    else:
        return False

def drum(score, value):
    if value == 'Банкрот':
        return 0
    else:
        return score + value

def compare(curent_view):
    for i in range(0, len(curent_view)):
        if curent_view[i] == '*':
            return False
    return True

def check_letter(letter):
    rus_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                   "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    if letter in rus_letters:
        return True
    else:
        return False

def main():
    answer, question = get_question(random.randrange(0, 1))
    score = 0
    curent_view = encrypt(answer)
    win = False
    print(question+ '? '+ "".join(curent_view))
    while True:
        print('Вращайте барабан')
        time.sleep(2)
        l_drum = [100, 200, 500, 'Банкрот']
        value = l_drum[random.randrange(0, len(l_drum))]
        score = drum(score, value)
        tem = input('Вы готовы назвать слово? ').lower()
        if tem == 'да':
            word = input('Ввыедите слово ').lower()
            if guess_word(answer, word):
                win = True
            else:
                print('Неверно. Вы проиграли, ваш счет: '+ str(score))
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
            print('Вы победили со счетом: '+ str(score))
            break

main()