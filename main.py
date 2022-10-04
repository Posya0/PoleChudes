import random


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