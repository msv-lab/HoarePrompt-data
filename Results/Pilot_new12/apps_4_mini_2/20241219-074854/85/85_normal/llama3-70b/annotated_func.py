#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 10^9.
def func():
    n = int(input())
    ans = 0
    for i in range(1, n // 2 + 1):
        if (i + (n - i)) % 10 ** (len(str(i + (n - i))) - 1) == 0:
            ans += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 10^9, `ans` is the count of values of `i` in the range from 1 to `n // 2` for which `(i + (n - i))` is a multiple of `10` raised to the power of `(len(str(i + (n - i))) - 1)`, `i` is 1 at the start and iterates up to `n // 2`.
    print(ans)
#Overall this is what the function does:The function reads an integer input `n` (where 2 ≤ n ≤ 10^9) and calculates the count of integers `i` in the range from 1 to `n // 2` inclusive for which the sum `(i + (n - i))`, which simplifies to `n`, is a multiple of `10` raised to the power of `(len(str(n)) - 1)`. It prints out this count (`ans`). The function does not return a value; it only outputs the result. It lacks input validation for edge cases, such as handling invalid or non-integer inputs and does not address the scenario when `n` is outside the specified bounds. The output will be `0` if no valid `i` values meet the condition, or a positive integer denoting the count of such `i` values.

