#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `res` is equal to the total number of divisors of `n`, `n` is a positive integer such that 1 <= `n` <= 10^9.
    print(res)
#Overall this is what the function does:The function accepts a positive integer `n` through user input, calculates the total number of divisors of `n`, and prints this total. The function does not return any value and handles edge cases by correctly counting divisors including perfect squares, ensuring the count is accurate for all integers within the specified range.

