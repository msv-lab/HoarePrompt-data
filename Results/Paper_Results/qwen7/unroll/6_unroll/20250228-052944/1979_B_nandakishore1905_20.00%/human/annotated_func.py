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
        
    #State: Output State: The output state will consist of a series of numbers printed for each iteration of the loop based on the conditions provided in the loop body. For each test case, the output will be either `k`, `1`, `2`, or `k - q` depending on the values of `n` and `m`. Here, `k` is the absolute difference between `n` and `m`, `q` is calculated as \(2^{(p-1)}\) where `p` is the length of the binary representation of `k` without the '0b' prefix.
#Overall this is what the function does:The function processes a series of test cases, each containing two distinct non-negative integers \(n\) and \(m\). For each test case, it calculates the absolute difference \(k\) between \(n\) and \(m\), and then prints one of four possible values based on specific conditions involving \(k\): \(k\), \(1\), \(2\), or \(k - q\), where \(q\) is derived from the binary representation of \(k\). The function does not return any value but outputs these results for each test case.

