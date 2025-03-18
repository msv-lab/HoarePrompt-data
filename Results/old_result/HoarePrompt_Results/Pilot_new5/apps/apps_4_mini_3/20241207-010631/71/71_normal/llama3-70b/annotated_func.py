#State of the program right berfore the function call: n is a non-negative integer (0 ≤ n ≤ 2,000,000,000) and k is a positive integer (1 ≤ k ≤ 9).
def func():
    n, k = map(int, input().split())
    w = 0
    while n % 10 ** k != 0:
        w += 1
        
        n //= 10
        
    #State of the program after the loop has been executed: 'n' is 0 and 'w' is the number of digits in the original value of 'n' if n was less than 10^k or 'k' if n was greater than or equal to 10^k
    print(w)
#Overall this is what the function does:The function accepts a non-negative integer `n` and a positive integer `k`. It calculates the number of digits removed from `n` until `n` becomes divisible by 10 raised to the power of `k`. The function then prints the count of digits removed (`w`). If `n` is already divisible by 10^k, it returns 0 since no digits need to be removed. The final value of `w` represents how many digits were discarded before reaching divisibility, up to a maximum of `k`.

