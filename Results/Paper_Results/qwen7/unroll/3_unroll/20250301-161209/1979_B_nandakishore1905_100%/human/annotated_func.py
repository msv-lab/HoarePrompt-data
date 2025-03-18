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
        
    #State: Output State: The output state will consist of a series of integers printed for each test case within the loop. For each test case, the value of `k` (which is the absolute difference between `n` and `m`) will determine the output based on specific conditions. If `k` is a power of 2, it will print `k`. If `k` is odd, it will print `1`. If `k` is even but not a power of 2, it will find the highest power of 2 less than or equal to `k`, subtract that from `k`, and continue this process until `k` becomes a power of 2 or 1, then print the final value of `k`.
    #
    #In summary, the output will be a sequence of integers, either the original `k`, `1`, or the result of the described process for each test case.
#Overall this is what the function does:The function processes a series of test cases where for each case, two integers \( n \) and \( m \) are provided. It calculates the absolute difference \( k \) between \( n \) and \( m \). Depending on the value of \( k \), it prints one of three possible outcomes: if \( k \) is a power of 2, it prints \( k \); if \( k \) is odd, it prints 1; otherwise, it finds the highest power of 2 less than or equal to \( k \), subtracts it from \( k \), and repeats the process until \( k \) becomes a power of 2 or 1, then prints the final value of \( k \). The function does not return any value but prints the results for each test case.

