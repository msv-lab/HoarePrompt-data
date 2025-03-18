#State of the program right berfore the function call: n is a non-negative integer such that 0 ≤ n ≤ 2,000,000,000, and k is a positive integer such that 1 ≤ k ≤ 9.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is a multiple of 10
    print(w)
#Overall this is what the function does:The function reads two integers, `n` (a non-negative integer) and `k` (a positive integer), from input. It counts how many times `n` can be divided by 10 before it becomes a multiple of `10^k`. This count is stored in the variable `w` and is printed at the end. After the function concludes, `n` will be a multiple of `10^k`, and `w` will indicate how many times the division occurred. If `n` is already a multiple of `10^k`, `w` will be 0. The edge case of `n` being 0 should also be considered, as it is a valid input which would lead to an immediate exit from the loop (thus `w` would also be 0). The function doesn't return a value; it merely prints the result.

