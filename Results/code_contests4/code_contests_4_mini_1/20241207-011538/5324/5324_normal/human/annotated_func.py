#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^5, and a is a list of 2 * n integers where each integer a_i satisfies 1 ≤ a_i ≤ n and every number from 1 to n appears exactly twice in the list.
def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `y` is 0, `x` is the greatest common divisor (GCD) of the original values of `x` and `y`
    return x
    #The program returns the greatest common divisor (GCD) of the original values of x and y, where y is 0. Since the GCD of any number and 0 is the number itself, the program returns x.
#Overall this is what the function does:The function accepts two integers `x` and `y`, and returns the greatest common divisor (GCD) of `x` and `y`. If `y` is 0, the function returns `x`, which is consistent with the mathematical definition of GCD. The GCD is computed using the Euclidean algorithm, which repeatedly replaces `x` and `y` with `y` and `x % y` until `y` becomes 0. The function does not handle cases where `x` or `y` are negative, which can lead to unexpected results as GCD is typically defined only for non-negative integers.

#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100000, and a is a list of 2 * n integers where each integer a_i satisfies 1 ≤ a_i ≤ n, with each integer from 1 to n appearing exactly twice in the list.
def func_2():
    n = int(input())
    a = sorted(zip(map(int, input().split()), range(1, 2 * n + 1)))
    dist = 0
    prev = 1
    for i in range(n):
        pos = a[2 * i][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `dist` is the total distance computed as the accumulated sum of absolute differences, `prev` is equal to `a[2 * (n - 1)][1]`, `pos` is equal to `a[2 * (n - 1)][1]`.
    prev = 1
    for i in range(n):
        pos = a[2 * i + 1][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `dist` is the total distance computed as the accumulated sum of absolute differences, `prev` is `a[2 * (n - 1) + 1][1]`, `pos` is `a[2 * (n - 1) + 1][1]`.
    print(dist)
#Overall this is what the function does:The function accepts a positive integer `n` and a list `a` of `2 * n` integers, where each integer in the range from 1 to `n` appears exactly twice. It calculates the total distance based on the positions of these integers in the sorted list, by summing the absolute differences between consecutive positions of both the first and second occurrences of each integer, and then prints this total distance.

