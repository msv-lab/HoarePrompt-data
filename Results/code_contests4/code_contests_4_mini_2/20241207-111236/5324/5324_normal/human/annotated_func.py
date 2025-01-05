#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^5, and a is a list of 2*n integers where each integer a_i (1 ≤ a_i ≤ n) occurs exactly twice.
def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the greatest common divisor (GCD) of the initial values of `x` and `y`, and `n` is a positive integer such that 1 ≤ `n` ≤ 10^5; `a` is a list of 2*`n` integers where each integer `a_i` (1 ≤ `a_i` ≤ `n`) occurs exactly twice.
    return x
    #The program returns the greatest common divisor (GCD) of the initial values of x and y, where y is 0 and x is the GCD itself.
#Overall this is what the function does:The function accepts two integers `x` and `y`, and returns the greatest common divisor (GCD) of the initial values of `x` and `y`. The function operates correctly for any pair of non-negative integers, including cases where either `x` or `y` is zero. If `x` is zero, the GCD returned will be the absolute value of `y`, and if both are zero, it conventionally returns zero, although the behavior of GCD(0, 0) is mathematically undefined.

#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^5, and a is a list of 2*n integers where each integer a_i (1 ≤ a_i ≤ n) appears exactly twice.
def func_2():
    n = int(input())
    a = sorted(zip(map(int, input().split()), range(1, 2 * n + 1)))
    dist = 0
    prev = 1
    for i in range(n):
        pos = a[2 * i][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `pos` is equal to `a[2 * (n - 1)][1]`, `dist` is the total distance calculated, `prev` is equal to `pos`.
    prev = 1
    for i in range(n):
        pos = a[2 * i + 1][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n`, `pos` is equal to `a[2 * (n - 1) + 1][1]`, `dist` is the total distance calculated from all iterations, `prev` is equal to `pos` after the last iteration.
    print(dist)
#Overall this is what the function does:The function accepts a positive integer `n` and calculates the total distance traversed by moving to the positions of a list of 2*n integers, where each integer appears exactly twice. It computes the distance by first moving to the positions of the first occurrences and then to the positions of the second occurrences of the integers in the sorted list. Finally, it prints the total distance.

