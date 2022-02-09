# Pytest sample program
import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 50
def test_square():
   num=5
   assert num*num==20