from generic_test_engine import generic_test_engine
__author__ = 'bruno'

def test_double_char():
    test_matrix = [
        ('The','TThhee'),
        ('AAbb','AAAAbbbb'),
        ('Hi-There','HHii--TThheerree'),
    ]
    generic_test_engine(test_matrix,double_char,unpack=False)
    
def double_char(s): return "".join([ch*2 for ch in s])
    
print ("Testing double_char")
test_double_char()