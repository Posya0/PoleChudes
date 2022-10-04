from main import *

def test_1():
    try:
        a,q = get_question(1)
        assert a == "лена" and q ==  "река в Сибири"
    except:
        print('test error')
    else:
        print('test passed')

test_1()