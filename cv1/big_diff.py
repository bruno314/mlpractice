from generic_test_engine import generic_test_engine
__author__ = 'bruno'

def test_big_diff():
    test_matrix = [
        ([10,3,5,6],7),
        ([7,2,10,9],8),
        ([2,10,7,2],8),
    ]
    generic_test_engine(test_matrix,big_diff,unpack=False)

def big_diff(arr): return max(arr)-min(arr)

print ("Testing big_diff")
test_big_diff()