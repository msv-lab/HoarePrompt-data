#State of the program right berfore the function call: The function should accept two parameters, n and m, where n and m are integers such that 1 <= n, m <= 100.
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
        
    #State: The values of `n` and `m` will be the last pair of integers read from the input during the final iteration of the loop. The value of `t` will remain unchanged. The loop will have printed 'Yes' or 'No' for each iteration based on the conditions specified in the loop body.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads a pair of integers `n` and `m` from the input. The function then prints 'Yes' or 'No' based on the following conditions for each pair: if `n` equals `m`, if `m` is `n - 1`, or if both `n` and `m` are either even or odd. After processing all test cases, the function does not return any value. The final state of the program is that the values of `n` and `m` will be the last pair of integers read from the input during the final iteration of the loop, and `t` will remain unchanged.

