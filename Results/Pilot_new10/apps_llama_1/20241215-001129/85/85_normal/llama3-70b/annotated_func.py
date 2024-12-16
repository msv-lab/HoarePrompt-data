#State of the program right berfore the function call: There exists a positive integer n representing the number of shovels in Polycarp's shop, 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is the original input integer, `ans` is the number of integers `i` between 1 and `n // 2` (inclusive) for which `n` is divisible by `10` raised to the power of the number of digits in `n` minus 1, and `i` is `n // 2`.
    print(ans)
#Overall this is what the function does:The function takes an integer input `n` from the user, calculates the number of times `n` can be divided by `10` raised to the power of the number of digits in `n` minus 1 without a remainder, and prints this count. However, due to the nature of the condition, the count will either be `n // 2` if the divisibility condition is met or 0 if it is not, essentially making the loop's outcome dependent solely on whether `n` meets the specific divisibility criterion.

