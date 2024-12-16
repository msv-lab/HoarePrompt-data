#State of the program right berfore the function call: There is one input variable, n, which is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `n` is an integer, `i` is the integer part of the square root of `n`, `res` is the number of divisors of `n`, considering that if `n` is a perfect square, its square root is counted only once.
    print(res)
#Overall this is what the function does:The function accepts an integer input `n` from the user, calculates the total number of divisors of `n`, counting the square root of `n` only once if `n` is a perfect square, and prints this count.

