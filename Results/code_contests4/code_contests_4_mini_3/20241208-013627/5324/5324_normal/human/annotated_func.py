#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^5, and a is a list of 2 * n integers where each integer a_i (1 ≤ a_i ≤ n) occurs exactly twice.
def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^5; `a` is a list of 2 * `n` integers where each integer `a_i` (1 ≤ `a_i` ≤ `n`) occurs exactly twice; `x` is the greatest common divisor of the initial values of `x` and `y`, and `y` is 0.
    return x
    #The program returns the greatest common divisor of the initial values of x and y, where y is 0. Since the GCD of any number and 0 is the number itself, the program returns the initial value of x.
#Overall this is what the function does:The function accepts two integers `x` and `y` and computes their greatest common divisor (GCD) using the Euclidean algorithm. It returns the GCD of the initial values of `x` and `y`. If `y` is 0, the function returns `x`, which is the GCD of any number and 0. The function correctly handles cases where `y` may initially be 0, returning `x` immediately in that case.

#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, and a is a list of 2 ⋅ n integers where each integer a_i satisfies 1 ≤ a_i ≤ n and each integer from 1 to n occurs exactly twice.
def func_2():
    n = int(input())
    a = sorted(zip(map(int, input().split()), range(1, 2 * n + 1)))
    dist = 0
    prev = 1
    for i in range(n):
        pos = a[2 * i][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `prev` is equal to the value of `a[2 * (n - 1)][1]` if `n` is greater than 0, `dist` is the sum of absolute differences calculated during the loop, and if `n` is 0, `dist` is 0 and `prev` is 1.
    prev = 1
    for i in range(n):
        pos = a[2 * i + 1][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `prev` is `a[2n-1][1]`, `dist` is the total of distances calculated during the loop, `n` is a non-negative integer.
    print(dist)
#Overall this is what the function does:The function accepts an integer `n` and a list `a` that contains `2 * n` integers, where each integer from 1 to `n` occurs exactly twice. It calculates the total distance traveled through the positions of these integers in the sorted list, by summing the absolute differences between consecutive positions of each integer's occurrences, and prints the total distance. The function does not handle cases where the input constraints are not met, such as if `n` is outside the range 1 to 100,000 or if the list does not contain the required integers.

