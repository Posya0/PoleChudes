from main import *


def test_1():
    try:
        a, q = get_question(1)
        assert a == "лена" and q == "река в Сибири"
    except:
        print('test error')
    else:
        print('test passed')


def test_2():
    try:
        t = encrypt('well')
        assert t == ['*', '*', '*', '*']
    except:
        print('test error')
    else:
        print('test passed')


def test_3_1():
    try:
        t = guess_letter('word', ['*', '*', '*', '*'], 'o')
        assert t == ['*', 'o', '*', '*']
    except:
        print('test error')
    else:
        print('test passed')


def test_3_2():
    try:
        t = guess_letter('word', ['*', '*', '*', '*'], 'к')
        assert t == ['*', '*', '*', '*']
    except:
        print('test error')
    else:
        print('test passed')


def test_3_3():
    try:
        t = guess_letter('слово', ['*', '*', '*', '*', '*'], 'о')
        assert t == ['*', '*', 'о', '*', 'о']
    except:
        print('test error')
    else:
        print('test passed')


def test_4_1():
    try:
        assert guess_word("слово", "слово")
    except:
        print('test error')
    else:
        print('test passed')


def test_4_2():
    try:
        t = guess_word("слово", "слова")
        assert t != True
    except:
        print('test error')
    else:
        print('test passed')


def test_5_1():
    try:
        t = drum(100, 100)
        assert t == 200
    except:
        print('test error')
    else:
        print('test passed')


def test_5_2():
    try:
        t = drum(0, 1000)
        assert t == 1000
    except:
        print('test error')
    else:
        print('test passed')


def test_5_2():
    try:
        t = drum(1000, 'Банкрот')
        assert t == 0
    except:
        print('test error')
    else:
        print('test passed')


def test_6_1():
    try:
        assert not compare(['*', '*', '*', '*'])
    except:
        print('test error')
    else:
        print('test passed')


def test_6_2():
    try:
        assert compare(['w', 'o', 'r', 'd'])
    except:
        print('test error')
    else:
        print('test passed')


def test_6_3():
    try:
        assert not compare(['w', 'o', '*', 'd'])
    except:
        print('test error')
    else:
        print('test passed')


def test_7_1():
    try:
        assert check_letter('а')
    except:
        print('test error')
    else:
        print('test passed')


def test_7_2():
    try:
        assert check_letter('ё')
    except:
        print('test error')
    else:
        print('test passed')


def test_7_3():
    try:
        assert not check_letter('b')
    except:
        print('test error')
    else:
        print('test passed')


test_1()
test_2()
test_3_1()
test_3_2()
test_3_3()
test_4_1()
test_4_2()
test_5_1()
test_5_2()
test_6_1()
test_6_2()
test_6_3()
test_7_1()
test_7_2()
test_7_3()
