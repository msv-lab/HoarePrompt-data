#State of the program right berfore the function call: n is a non-negative integer less than or equal to 2,000,000,000, and k is an integer such that 1 <= k <= 9.
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: `n` is the largest multiple of `10^k` less than or equal to the original `n`, or the original `n` if it's less than `10^k`, and `w` is the number of digits removed from the original `n` to reach this value, or 0 if the original `n` is less than `10^k` or already a multiple of `10^k`.
    print(w)
#Overall this is what the function does:The function accepts two integer parameters, `n` and `k`, where `n` is a non-negative integer less than or equal to 2,000,000,000 and `k` is an integer between 1 and 9, and returns the number of digits removed from `n` to reach the largest multiple of `10^k` less than or equal to `n`. If `n` is less than `10^k`, the function returns the number of digits in `n`. The function handles edge cases where `n` is 0 or a multiple of `10^k`, returning 0 in these cases. After execution, the program state is such that the original `n` has been modified and replaced by its largest multiple of `10^k` less than or equal to `n`, but this modified value is not returned, and instead, the number of digits removed from `n` to reach this value is printed.

