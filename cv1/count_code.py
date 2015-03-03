__author__ = 'bruno'
from generic_test_engine import generic_test_engine
import re

def test_count_code():
    test_matrix = [
        ("aaacodebbb",1),
        ("codexxcode",2),
        ("cozexxcope",2),
    ]
    generic_test_engine(test_matrix,count_code,unpack=False)
    
def count_code(s): return len(re.findall(r"co.e",s,re.UNICODE))

print("Testing count_code")
test_count_code()