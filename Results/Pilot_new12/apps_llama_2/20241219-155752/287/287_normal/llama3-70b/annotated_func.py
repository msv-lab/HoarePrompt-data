#State of the program right berfore the function call: The input is an integer n, such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 10^9, `i` is the largest number less than or equal to the square root of `n`, `res` is the number of divisors of `n`, minus 1 if `n` is a perfect square.
    print(res)
#Overall this is what the function does:The function calculates and prints the total number of divisors of a given integer input `n`, with a correction to account for perfect squares by subtracting 1 from the count. It accepts an integer `n` through user input, such that `1 <= n <= 10^9`, and does not return any value. After execution, the program has printed the total number of divisors of `n` to the console.

