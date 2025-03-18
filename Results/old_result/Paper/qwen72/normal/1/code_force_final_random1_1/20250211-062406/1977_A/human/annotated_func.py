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
        
    #State: `t` is an input integer between 1 and 100, `i` is `t - 1`, `n` is the first integer from the last input, and `m` is the second integer from the last input. The values of `n` and `m` will depend on the final input provided during the last iteration of the loop. If `n` == `m`, the values of `n` and `m` remain unchanged. If `m` > `n`, the values of `n` and `m` remain unchanged. If `m` <= `n`, and specifically if `m` equals `n - 1`, the values of `n` and `m` remain unchanged. If `m` does not equal `n - 1`, the values of `n` and `m` are maintained regardless of whether they are even or odd.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases, where 1 ≤ t ≤ 100. For each test case, it reads two integers `n` and `m` (1 ≤ n, m ≤ 100) from the input. It then evaluates the relationship between `n` and `m` and prints 'Yes' or 'No' based on the following conditions: if `n` equals `m`, or `m` equals `n - 1`, or both `n` and `m` are even, or both `n` and `m` are odd, it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, the function completes, and the final state includes the values of `t`, `i` (which is `t - 1`), `n`, and `m` from the last test case. The function does not return any value.

