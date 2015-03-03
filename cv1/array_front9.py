from generic_test_engine import generic_test_engine

def test_array_front9():
    test_matrix = [
        ([1,2,9,3,4],True),
        ([1,2,3,4,9],False),
        ([1,2,3,4,5],False),
    ]
    generic_test_engine(test_matrix,array_front9,unpack=False)
    
def array_front9(arr): return 9 in arr[0:min(4,len(arr))]

print ("Testing array_front9")
test_array_front9()



