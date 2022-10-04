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

