#State of the program right berfore the function call: n is a non-negative integer between 0 and 2,000,000,000 inclusive, and k is a positive integer between 1 and 9 inclusive.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is an integer that is divisible by `10
    print(w)
#Overall this is what the function does:The function accepts two parameters: a non-negative integer `n` (between 0 and 2,000,000,000 inclusive) and a positive integer `k` (between 1 and 9 inclusive). It counts the number of digits that need to be removed from the right end of `n` until `n` becomes divisible by `10^k`, and it prints this count. If `n` is already divisible by `10^k` at the start, it returns 0 without removing any digits.

