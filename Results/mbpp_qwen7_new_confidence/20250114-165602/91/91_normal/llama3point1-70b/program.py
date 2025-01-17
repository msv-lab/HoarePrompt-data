import math

def next_power_of_2(n):
    return 2 ** math.ceil(math.log2(n + 1))
