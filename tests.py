from main import *

def test_1():
    try:
        a,q = get_question(1)
        assert a == "лена" and q ==  "река в Сибири"
    except:
        print('test error')
    else:
        print('test passed')

def test_2():
    try:
        t = encrypt('well')
        assert t == ['*','*','*','*']
    except:
        print('test error')
    else:
        print('test passed')

def test_3():
    try:
        t = guess_letter('word', ['*','*','*','*'], 'o')
        assert t == ['*','o','*','*']
    except:
        print('test error')
    else:
        print('test passed')

test_1()
test_2()
test_3()