#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer within the range 1 to 10^9, `res` is the total number of divisors of `n`.
    print(res)
#Overall this is what the function does:The function reads a positive integer `n` (where \( 1 \leq n \leq 10^9 \)) from user input and calculates the total number of divisors of `n`. It iterates through all integers from 1 up to the square root of `n` to identify divisors. For each divisor found, it increases the count `res` by 2 for both the divisor and its complementary divisor. If the divisor is the square root of `n`, it adjusts the count by subtracting 1 to avoid double-counting. After completing the calculations, the function outputs the total count of divisors `res`. The function does not account for any invalid input scenarios, as it assumes proper input according to the problem statement.

