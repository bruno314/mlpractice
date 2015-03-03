from generic_test_engine import generic_test_engine
__author__ = 'bruno'


def test_count_evens():
    test_matrix = [
        ([2,1,2,3,4],3),
        ([2,2,0],3),
        ([1,3,5],0),
    ]
    generic_test_engine(test_matrix,count_evens,unpack=False)
    
def count_evens(arr): return sum(list(map(lambda _:(1+_)%2,arr)))

print ("Testing count_evens")
test_count_evens()


