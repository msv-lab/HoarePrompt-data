#State of the program right berfore the function call: x and y are distinct non-negative integers such that 0 <= x, y <= 10^9 and x ≠ y.
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
        
    #State: The loop has executed `int(input())` times, and for each iteration `i` from 0 to `int(input()) - 1`, the following conditions were checked: `n` and `m` are input integers greater than 0, `k` is the absolute difference between `n` and `m`. If `k` is a power of 2, the value of `k` was printed. If `k` is not a power of 2 and `n` is 0, the value 1 or 2 was printed depending on whether `m` is odd or even, respectively. Otherwise, the value `k - 2
#Overall this is what the function does:The function reads a number of test cases from the user, and for each test case, it reads two integers `n` and `m`. It then calculates the absolute difference `k` between `n` and `m`. If `k` is a power of 2, it prints `k`. If `k` is not a power of 2 and `n` is 0, it prints 1 if `m` is odd, and 2 if `m` is even. Otherwise, it prints the value `k - 2^(p-1)`, where `p` is the number of bits in the binary representation of `k`. The function does not return any values; it only prints the results for each test case.

