#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers where 1 ≤ n, k ≤ 10^18.
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
        
    #State: The value of t is 0, and for each test case, the values of n and k are processed and the corresponding output ('YES' or 'NO') is printed based on the conditions in the loop. The values of n and k for each test case are not retained after the loop completes.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two positive integers `n` and `k` from the input. It then checks if `n` equals `k`, and if so, prints 'YES' followed by two lines, each containing the number 1. If `n` does not equal `k` but `n + 2` is greater than `k * 2`, it prints 'YES' followed by two lines: the first line contains `n - k + 1`, and the second line contains 1. If neither condition is met, it prints 'NO'. After processing all test cases, the function does not retain the values of `n` and `k` for each test case, and the value of `t` is 0.

