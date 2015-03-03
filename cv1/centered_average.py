from generic_test_engine import generic_test_engine
__author__ = 'bruno'


def test_centered_average():
    test_matrix = [
        ([1, 2, 3, 4, 100],3),
        ([1, 1, 5, 5, 10, 8, 7],5),
        ([-10, -4, -2, -4, -2, 0],-3),
    ]
    generic_test_engine(test_matrix,centered_average,unpack=False)
    
def centered_average(arr): return (sum(arr)-max(arr)-min(arr)) // (len(arr)-2)
    
print ("Testing centered_average")
test_centered_average()