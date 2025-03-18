#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, and for each test case, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: t is an integer where 1 <= t <= 1000, and for each test case, k, x, and a are integers such that 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9. The loop has executed all iterations, and for each test case, it has printed 'Yes' if a is greater than or equal to the calculated value of s, otherwise it has printed 'No'. The values of k, x, and a for each test case remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from input, representing the number of test cases. For each test case, it reads three integers `k`, `x`, and `a` from input. It then calculates a value `s` based on `k` and `x` and prints 'Yes' if `a` is greater than or equal to `s`, otherwise it prints 'No'. After processing all test cases, the function completes, and the values of `k`, `x`, and `a` for each test case remain unchanged.

