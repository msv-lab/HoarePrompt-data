#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, x and y are distinct non-negative integers such that 0 ≤ x, y ≤ 10^9.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: Output State: The output state will consist of a series of lines, each containing either `k`, `1`, `2`, or `k - q`, where `k` is the absolute difference between `n` and `m` for each iteration of the loop. The specific value printed depends on the conditions met by `n` and `m`. If `k` is a power of 2, it prints `k`. If `n` is 0 and `m` is odd, it prints `1`. If `n` is 0 and `m` is even, it prints `2`. Otherwise, it calculates `q` as the highest power of 2 less than `k` and prints `k - q`.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers \( n \) and \( m \). For each test case, it calculates the absolute difference \( k \) between \( n \) and \( m \). Depending on the value of \( k \), it prints one of four possible values: \( k \), \( 1 \), \( 2 \), or \( k - q \), where \( q \) is the highest power of 2 less than \( k \). If \( k \) is a power of 2, it prints \( k \). If \( n \) is 0 and \( m \) is odd, it prints 1. If \( n \) is 0 and \( m \) is even, it prints 2. Otherwise, it calculates \( q \) and prints \( k - q \). The function does not return any value; instead, it outputs the results directly.

