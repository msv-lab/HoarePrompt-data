#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4, and for each test case, x and y are distinct non-negative integers such that 0 <= x, y <= 10^9.
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
        
    #State: Output State: The output state will consist of a series of integers printed for each iteration of the loop based on the conditions provided in the loop body. For each test case, the output will be either `k`, `1`, `2`, or `k - q` where `k` is the absolute difference between `n` and `m`, `q` is calculated as \(2^{(p-1)}\) with `p` being the length of the binary representation of `k` without the '0b' prefix.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two distinct non-negative integers \(n\) and \(m\). It calculates the absolute difference \(k\) between \(n\) and \(m\), and based on certain conditions, prints one of the following outputs for each test case: \(k\), \(1\), \(2\), or \(k - q\), where \(q\) is derived from the binary representation of \(k\). The function reads the number of test cases from the first line of input, followed by pairs of integers for each test case.

