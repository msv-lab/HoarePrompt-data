#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
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
        
    #State: Output State: The output state will consist of a series of 'Yes' and 'No' based on the conditions evaluated in each iteration of the loop. For each line of input provided during the loop, the program checks the relationship between `n` and `m`, and prints 'Yes' or 'No' accordingly. If `t` is the number of iterations, there will be `t` lines of output, each either 'Yes' or 'No', depending on the values of `n` and `m` for that iteration.
#Overall this is what the function does:The function processes a series of test cases defined by the integer `t`. For each test case, it reads two integers `n` and `m`, and prints 'Yes' or 'No' based on specific conditions. Specifically, it prints 'Yes' if `n` equals `m`, `m` is greater than `n` by exactly 1, both `n` and `m` are even, or both `n` and `m` are odd; otherwise, it prints 'No'. After processing all `t` test cases, the function concludes with a series of 'Yes' and 'No' outputs corresponding to the conditions evaluated for each pair of `n` and `m`.

