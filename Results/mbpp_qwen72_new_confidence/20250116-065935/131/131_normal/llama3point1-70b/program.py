def even_Power_Sum(n: int) -> int:
    return sum([i**5 for i in range(2, 2*n+1, 2)])
