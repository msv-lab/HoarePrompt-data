#State of the program right berfore the function call: t is an integer where 1 <= t <= 100, and for each test case, n and m are integers where 1 <= n, m <= 100.
def func():
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        
        if n == m:
            print('Yes')
        elif m > n:
            print('No')
        elif m == n - 1:
            print('Yes')
        elif m % 2 == 0 and n % 2 == 0:
            print('Yes')
        elif m % 2 != 0 and n % 2 != 0:
            print('Yes')
        else:
            print('No')
        
    #State: The value of `t` remains unchanged, and for each test case, the values of `n` and `m` are processed according to the conditions in the loop, printing 'Yes' or 'No' based on the given rules. The final state of `n` and `m` is undefined as they are reassigned in each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, where `1 <= t <= 100`, and then processes `t` test cases. For each test case, it reads two integers `n` and `m` from user input, where `1 <= n, m <= 100`. Based on the values of `n` and `m`, it prints 'Yes' if `n == m`, `m == n - 1`, both `n` and `m` are even, or both `n` and `m` are odd. Otherwise, it prints 'No'. The function does not return any value, and the final state of `n` and `m` is undefined as they are reassigned in each iteration.

