#State of the program right berfore the function call: n is a non-negative integer within the range 0 to 2,000,000,000, and k is a positive integer such that 1 <= k <= 9.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is the result of integer division of the original value of `n` by `10^w`, `w` is the count of how many times digits were removed until `n` became a multiple of `10^k`. If the original value of `n` was a multiple of `10^k`, the loop will not execute and `w` will remain 0.
    print(w)
#Overall this is what the function does:The function accepts no parameters and reads two integers, `n` and `k`, from input. It counts how many digits must be removed from the end of `n` to make it a multiple of `10^k`. The count of removed digits, `w`, is then printed. If `n` is already a multiple of `10^k`, no digits are removed and `w` remains 0. The function handles non-negative integers for `n` and ensures `k` is within the specified range of 1 to 9. It does not handle cases such as providing invalid input (e.g., non-integers or out-of-range values) or executing without input, which could result in an error. The final output is the integer value of `w`, reflecting the number of digits removed.

