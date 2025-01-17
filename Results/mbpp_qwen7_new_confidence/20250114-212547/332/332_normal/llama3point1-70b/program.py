def odd_num_sum(n):
    return sum((2*i-1)**4 for i in range(1, n+1))
