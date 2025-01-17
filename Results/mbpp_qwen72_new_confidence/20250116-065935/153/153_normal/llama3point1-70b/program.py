import math

def count_binary_seq(n):
    total_combinations = 2 ** (2 * n)
    half_combinations = total_combinations / 2
    return half_combinations