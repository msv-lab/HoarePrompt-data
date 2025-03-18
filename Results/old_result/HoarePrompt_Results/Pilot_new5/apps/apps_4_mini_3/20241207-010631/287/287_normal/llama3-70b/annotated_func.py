#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `res` is the total number of divisors of `n`, `i` is equal to int(n
    print(res)
#Overall this is what the function does:The function accepts a positive integer input `n` provided by the user, calculates the total number of divisors of `n`, and prints this total. It correctly accounts for perfect squares by ensuring that the square root is only counted once if `n` is a perfect square. However, the function lacks error handling for invalid input and does not return any value, it only prints the result.

