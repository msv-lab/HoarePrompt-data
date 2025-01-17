import math

def dif_Square(n):
    for i in range(int(math.sqrt(n)), 0, -1):
        if i*i <= n:
            return True
    return False
