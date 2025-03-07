#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
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
        
    #State: After all iterations of the loop have finished, `t` will be 0, `n` will be an integer equal to the first number entered in the last iteration, and `k` will be an integer equal to the second number entered in the last iteration.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers \( n \) and \( k \). For each test case, it checks if \( n \) is equal to \( k \), or if \( n + 2 \) is greater than \( 2k \). If either condition is met, it prints 'YES' followed by specific values. Otherwise, it prints 'NO'. After processing all test cases, the function does not return any value but prints the results for each test case.

