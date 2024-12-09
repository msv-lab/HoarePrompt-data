#State of the program right berfore the function call: n is a non-negative integer within the range 0 ≤ n ≤ 2,000,000,000, and k is a positive integer within the range 1 ≤ k ≤ 9.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is divisible by `10
    print(w)
#Overall this is what the function does:The function accepts two integers, `n` (a non-negative integer) and `k` (a positive integer), read from input. It counts the number of times `n` can be divided by 10 until `n` becomes divisible by \(10^k\). The function then prints the count of such divisions without returning any value. If `n` starts off as already divisible by \(10^k\), the function will print `0`.

