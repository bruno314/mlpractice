from generic_test_engine import generic_test_engine
__author__ = 'bruno'

def test_front_times():
    test_matrix = [
        (['Chocolate', 2],'ChoCho'),
        (['Chocolate', 3],'ChoChoCho'),
        (['Abc', 3],'AbcAbcAbc'),
        (['xx',8],'xx'*8)
    ]
    generic_test_engine(test_matrix,front_times,unpack=True)

def front_times(s,n): return s[0:min(3,len(s))]*n

print ("Testing front_times")
test_front_times()