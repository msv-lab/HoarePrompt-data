#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `n` is an input integer within the range \(1 \leq n \leq 10^9\), and `res` is the total number of divisors of `n` (each counted as 2) minus the count of perfect square divisors (each counted as -1).
    print(res)
#Overall this is what the function does:The function calculates and returns the total number of divisors of an integer `n` (where \(1 \leq n \leq 10^9\)), with each divisor counted as 2, and subtracts the count of perfect square divisors (counted as -1). The function reads an integer `n` from the user, iterates through all numbers from 1 to the square root of `n`, checks if they are divisors of `n`, and updates the result accordingly. If a perfect square divisor is found, it adjusts the result by subtracting 1.

