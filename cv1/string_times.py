from generic_test_engine import generic_test_engine
__author__ = 'bruno'

def test_string2():
    test_matrix = [
        (["Hi",2],"HiHi"),
        (["Hi",3],"HiHiHi"),
        (["Hi",1],"Hi"),
    ]
    generic_test_engine(test_matrix,string2,unpack=True)

def string2(s,n): return s*n

print("Testing string2")
test_string2()