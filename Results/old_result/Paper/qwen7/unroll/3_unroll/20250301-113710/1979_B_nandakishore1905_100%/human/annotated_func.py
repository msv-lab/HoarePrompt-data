#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
def func():
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif k % 2 != 0:
            print(1)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            f = k - q
            while f & f - 1 != 0:
                l = bin(f).replace('0b', '')
                p = len(l)
                q = 2 ** (p - 1)
                f = f - q
            print(f)
        
    #State: Output State: The output state will consist of a series of numbers printed for each test case within the loop. For each test case, the value of `k` (which is the absolute difference between `n` and `m`) will determine the output:
    #
    #- If `k` is a power of 2, it will print `k`.
    #- If `k` is odd, it will print `1`.
    #- If `k` is even and not a power of 2, it will find the highest power of 2 less than or equal to `k`, subtract that power of 2 from `k`, and continue this process until `k` becomes a power of 2 or 1, then print the final value of `k`.
    #
    #Each line of output corresponds to the result of one test case.
#Overall this is what the function does:The function processes a series of test cases, each containing two distinct non-negative integers \( n \) and \( m \). It calculates the absolute difference \( k \) between \( n \) and \( m \). Based on the value of \( k \), it prints one of three possible outputs for each test case:
- If \( k \) is a power of 2, it prints \( k \).
- If \( k \) is odd, it prints 1.
- If \( k \) is even and not a power of 2, it repeatedly subtracts the highest power of 2 less than or equal to \( k \) until \( k \) becomes a power of 2 or 1, then prints the final value of \( k \).

The function does not return any value; instead, it prints the results for each test case.

