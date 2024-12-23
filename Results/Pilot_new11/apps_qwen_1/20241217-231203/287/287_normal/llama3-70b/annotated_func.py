#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, and `res` is the sum of 2 for each divisor of `n`, adjusted by subtracting 1 if `n` is a perfect square.
    print(res)
#Overall this is what the function does:The function calculates the number of divisors of a given integer \( n \) (where \( 1 \leq n \leq 10^9 \)), and if \( n \) is a perfect square, it subtracts one from the count. Specifically, for each divisor \( i \) of \( n \) (where \( 1 \leq i \leq \sqrt{n} \)), it increments the result by 2. If \( i \times i = n \), it decrements the result by 1 to adjust for the double counting of the square root. The function then prints the final count of divisors.

