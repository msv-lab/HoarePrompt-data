#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9, and k is a non-negative integer such that 0 ≤ k ≤ 8.
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: `n` is the smallest multiple of 10 that is greater than or equal to the original value of `n`, `k` is an input non-negative integer such that 0 ≤ `k` ≤ 8, `x` is equal to 10.
    print(n)
#Overall this is what the function does:The function accepts two integers, `n` (where 1 ≤ n ≤ 10^9) and `k` (where 0 ≤ k ≤ 8), reads them from input, and then computes the smallest multiple of 10^k that is greater than or equal to `n`. It prints this result, but does not return any value. If `n` is already a multiple of 10^k, it will print `n` without any changes.

