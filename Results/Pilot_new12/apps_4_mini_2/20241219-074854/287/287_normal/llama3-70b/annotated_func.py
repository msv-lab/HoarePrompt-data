#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    res = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res += 2
        
        if i * i == n:
            res -= 1
        
    #State of the program after the  for loop has been executed: `res` is equal to the total number of positive divisors of `n`, `n` is a positive integer between 1 and 10^9.
    print(res)
#Overall this is what the function does:The function reads a positive integer `n` from user input, where `1 <= n <= 10^9`. It calculates and prints the total number of positive divisors of `n`. The function does not handle negative or non-integer inputs, which could lead to unexpected behavior if such cases are encountered. The output will be the number of unique positive divisors of `n` displayed to the console. The function does not return any value; it only prints the result.

