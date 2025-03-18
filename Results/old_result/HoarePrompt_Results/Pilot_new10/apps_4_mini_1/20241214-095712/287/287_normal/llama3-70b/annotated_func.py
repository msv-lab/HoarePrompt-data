#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `res` is equal to the number of divisors of `n`, and `i` is int(n
    print(res)
#Overall this is what the function does:The function accepts an integer input `n` (1 <= n <= 10^9) and outputs the total number of divisors of `n`. It calculates the number of divisors by iterating from 1 to the square root of `n`, counting both the divisor and its complement, while adjusting for perfect squares. It does not return a value; instead, it prints the result directly.

