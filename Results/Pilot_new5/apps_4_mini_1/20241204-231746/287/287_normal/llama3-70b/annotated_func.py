#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `res` is the total number of divisors of `n`, which is `2 * k` if `n` is not a perfect square or `2 * k - 1` if `n` is a perfect square, where `k` is the number of distinct divisors of `n`.
    print(res)
#Overall this is what the function does:The function accepts a positive integer `n` from user input and prints the total number of divisors of `n`, adjusting for perfect squares by decrementing the count if necessary.

