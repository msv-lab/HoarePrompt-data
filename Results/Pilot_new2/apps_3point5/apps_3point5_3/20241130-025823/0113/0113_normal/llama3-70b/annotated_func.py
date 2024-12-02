#State of the program right berfore the function call: n is a positive integer and k is a non-negative integer such that 1 ≤ n ≤ 10^9 and 0 ≤ k ≤ 8.**
def func():
    n, k = map(int, input().split())
    x = 10 ** k
    while n % x != 0:
        n += 1
        
    #State of the program after the loop has been executed: After the loop executes, n is a positive integer that is not a multiple of 10 and has been increased by a certain number of times, k is a non-negative integer such that 1 ≤ n ≤ 10^9 and 0 ≤ k ≤ 8, x is 10 to the power of k+1
    print(n)
#Overall this is what the function does:The function `func` reads input values for `n` and `k`, where `n` is a positive integer and `k` is a non-negative integer within specified constraints. It then increments `n` until it becomes a multiple of 10 to the power of `k`. Finally, it prints the updated value of `n`. The function does not explicitly return any value. It ensures that `n` satisfies the condition of being a multiple of 10 to the power of `k`.

