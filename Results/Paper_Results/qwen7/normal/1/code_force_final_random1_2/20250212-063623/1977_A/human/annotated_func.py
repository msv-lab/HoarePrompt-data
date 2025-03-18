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
        
    #State: Output State: The variable `t` remains the same as its initial value, which is an integer between 1 and 100 inclusive. After all iterations of the loop, `i` will be equal to `t - 1`, since the loop runs `t` times. The variables `n` and `m` retain their values from the last iteration of the loop. Specifically, `n` is the first integer input by the user, and `m` is the second integer input by the user during the last iteration. The output of the loop depends on the values of `n` and `m` during the last iteration:
    #
    #- If `n` equals `m`, the output is 'Yes'.
    #- If `m` is greater than `n`, the output is 'No'.
    #- If `m` equals `n - 1`, the output is 'Yes'.
    #- If both `m` and `n` are even, the output is 'Yes'.
    #- If both `m` and `n` are odd, the output is 'Yes'.
    #- Otherwise, the output is 'No'.
    #
    #In summary, after all iterations of the loop, `t` remains unchanged, `i` is `t - 1`, and the final output of the loop is determined by the values of `n` and `m` from the last iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it checks specific conditions involving \( n \) and \( m \) and prints 'Yes' or 'No' based on these conditions. After processing all test cases, the function does not return any value but prints the results of the last test case. The variables \( t \), \( n \), and \( m \) retain their values from the last test case.

