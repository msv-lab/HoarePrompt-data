#State of the program right berfore the function call: x and n are integers such that 1 <= x < n <= 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: Postcondition: `x` is an integer such that \(1 \leq x < n \leq 10^9\), `i` is greater than or equal to the largest integer whose square is less than or equal to `x`, `n` is an integer such that \(1 \leq x < n \leq 10^9\), `output1` is a list containing all divisors of `x` from 1 up to the largest divisor less than or equal to \(\sqrt{x}\), `output2` is a list containing the corresponding quotients when `x` is divided by each divisor in `output1`.
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines the quotients when `x` is divided by each of its divisors from the largest divisor less than or equal to \(\sqrt{x}\) down to 1, followed by the divisors themselves.
#Overall this is what the function does:The function accepts an integer `x` and returns a list. This list contains the quotients of `x` divided by each of its divisors from the largest divisor less than or equal to \(\sqrt{x}\) down to 1, followed by the divisors themselves.

