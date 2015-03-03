from generic_test_engine import generic_test_engine
__author__ = 'bruno'

def test_end_other():
    test_matrix = [
        (['Hiabc', 'abc'],True),
        (['AbC', 'HiaBc'],True),
        (['abc', 'abXabc'],True),
    ]
    generic_test_engine(test_matrix,end_other,unpack=True)
    
def end_other(f,s): return f.lower()[::-1] == s.lower()[::-1][0:len(f)] or s.lower()[::-1] == f.lower()[::-1][0:len(s)]


print ("Testing end_other")
test_end_other()