from generic_test_engine import generic_test_engine
import re

__author__ = 'bruno'


def test_count_hi():
    test_matrix = [
        ('abc hi ho',1),
        ('ABChi hi',2),
        ('hihi',2),
    ]
    generic_test_engine(test_matrix,count_hi,unpack=False)
    
def count_hi(arr): return len(re.findall(r"hi",arr,re.UNICODE))

print ("Testing count_hi")
test_count_hi()