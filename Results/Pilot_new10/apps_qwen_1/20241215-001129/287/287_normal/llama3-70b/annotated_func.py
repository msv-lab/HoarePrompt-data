#State of the program right berfore the function call: The input is a single integer n where 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range \(1 \leq n \leq 10^9\), `res` is the number of divisors of `n` minus 1.
    print(res)
#Overall this is what the function does:The function reads an integer \( n \) (where \( 1 \leq n \leq 10^9 \)) and prints the number of divisors of \( n \). If \( n \) is a perfect square, one pair of divisors is subtracted to correct for double counting.

