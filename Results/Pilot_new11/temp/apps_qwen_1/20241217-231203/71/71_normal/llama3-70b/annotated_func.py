#State of the program right berfore the function call: The input consists of two integers n and k, where 0 ≤ n ≤ 2,000,000,000 and 1 ≤ k ≤ 9. The integer n is provided as a non-negative integer, and k is a positive integer indicating the power of 10 by which the resulting number must be divisible.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is `n // 10
    print(w)
#Overall this is what the function does:The function `func` accepts two parameters `n` (a non-negative integer where \(0 \leq n \leq 2,000,000,000\)) and `k` (a positive integer where \(1 \leq k \leq 9\)). It performs a series of operations to determine the number of times `n` needs to be divided by 10 until it becomes divisible by \(10^k\). After the loop, the function prints the count of divisions performed (`w`). The final state of the program is such that `n` is guaranteed to be divisible by \(10^k\), and the function does not return any value; instead, it prints the count of divisions required.

