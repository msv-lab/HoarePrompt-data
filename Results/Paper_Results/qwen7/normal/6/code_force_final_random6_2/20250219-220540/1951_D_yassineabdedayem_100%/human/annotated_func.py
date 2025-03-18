#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        if n == k:
            print('YES')
            print(1)
            print(1)
        elif n + 2 > k * 2:
            print('YES')
            print(2)
            print(n - k + 1, end=' ')
            print(1)
        else:
            print('NO')
        
    #State: Output State: The value of `t` remains unchanged, and it must be a positive integer not exceeding 1000. The variables `n` and `k` will hold the last values read from the input during the loop's final iteration. The output consists of 'YES' or 'NO' responses for each iteration, followed by either '1', '2', or no additional output depending on the conditions met in the loop. Specifically, if `n` equals `k`, it prints 'YES 1 1'. If `n + 2` is greater than `2k`, it prints 'YES 2' followed by `n - k + 1` and `1`. Otherwise, it prints 'NO'.
    #
    #This output state reflects the cumulative effect of the loop running its full course, with `t` iterations completed, and the final values of `n` and `k` being those from the last input line processed.
#Overall this is what the function does:The function processes up to 1000 test cases, where each test case consists of two positive integers \( n \) and \( k \). For each test case, it checks specific conditions involving \( n \) and \( k \) and prints either 'YES' or 'NO' along with some integers if applicable. If \( n \) equals \( k \), it prints 'YES 1 1'. If \( n + 2 \) is greater than \( 2k \), it prints 'YES 2' followed by \( n - k + 1 \) and 1. Otherwise, it prints 'NO'. After processing all test cases, the function does not return any value but outputs the results for each test case.

