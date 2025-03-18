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
        
    #State: `t` is an input integer where 1 <= t <= 100, `i` is `t-1`, `n` is an input integer, and `m` is an input integer. The loop has executed `t` times, and for each iteration, the values of `n` and `m` were read from input, and the conditions based on the relationship between `n` and `m` (equality, inequality, greater than, less than or equal to, etc.) were evaluated and printed accordingly.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases, where 1 <= t <= 100. For each test case, it reads two integers `n` and `m` (1 <= n, m <= 100) from the input. It then evaluates the relationship between `n` and `m` and prints 'Yes' or 'No' based on specific conditions: 'Yes' if `n` equals `m`, `m` is `n - 1`, both `n` and `m` are even, or both are odd; otherwise, it prints 'No'. After processing all `t` test cases, the function completes its execution.

