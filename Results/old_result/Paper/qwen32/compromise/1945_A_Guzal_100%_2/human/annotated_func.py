#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each of the t test cases, a, b, and c are non-negative integers such that 0 <= a, b, c <= 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: For each of the t test cases, the output will be either -1 or a calculated integer k based on the conditions provided in the loop. The value of t, a, b, c, and n remain unchanged except that for each iteration, the values of a, b, and c are read from the input. The variable k is recalculated in each iteration and printed accordingly.
#Overall this is what the function does:The function reads a positive integer `t` representing the number of test cases. For each test case, it reads three non-negative integers `a`, `b`, and `c`. It then calculates and prints either `-1` or a non-negative integer `k` based on the conditions provided. The value of `k` is calculated as `a` plus the integer division of the sum of `b` and `c` by 3, with an additional increment if the sum of `b` and `c` is not divisible by 3. The input values `t`, `a`, `b`, and `c` remain unchanged, and the function processes each test case independently.

