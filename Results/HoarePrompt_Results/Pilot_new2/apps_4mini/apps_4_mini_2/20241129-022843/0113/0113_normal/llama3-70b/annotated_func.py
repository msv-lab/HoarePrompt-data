#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^9, and k is a non-negative integer such that 0 ≤ k ≤ 8.
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: `n` is the smallest integer greater than or equal to the original value of `n` that is divisible by \(10^k\), and `n` will be equal to the original value of `n` plus the number of increments needed to make it divisible by \(x\)
    print(n)
#Overall this is what the function does:The function accepts no parameters directly but reads two integers from input: a positive integer `n` (where 1 ≤ n ≤ 10^9) and a non-negative integer `k` (where 0 ≤ k ≤ 8). It finds the smallest integer greater than or equal to `n` that is divisible by \(10^k\) and prints that integer. If `n` is already divisible by \(10^k\), it remains unchanged.

