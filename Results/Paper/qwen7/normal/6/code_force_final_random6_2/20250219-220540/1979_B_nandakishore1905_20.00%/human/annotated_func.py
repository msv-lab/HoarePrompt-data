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
        
    #State: After all iterations of the loop have finished, the value of `i` will be equal to `t`, `n` and `m` will be the last pair of input integers provided, `k` will be the absolute difference between the last `n` and `m`. If `k` is a power of 2, then `k` remains unchanged. Otherwise, if `n` is 0 and `m` is odd, then `n` is 0 and `m` is odd. In all other cases, `l` will be the binary string representation of `k` without the '0b' prefix, `p` will be the length of `l`, and `q` will be \(2^{(p - 1)}\).
#Overall this is what the function does:The function processes multiple test cases, each involving two distinct non-negative integers. For each test case, it calculates the absolute difference between the two integers. Depending on the value of this difference, it prints one of three possible outcomes: the difference itself if it is a power of 2, 1 if the first integer is 0 and the second is odd, or the difference minus the highest power of 2 less than or equal to the difference otherwise.

