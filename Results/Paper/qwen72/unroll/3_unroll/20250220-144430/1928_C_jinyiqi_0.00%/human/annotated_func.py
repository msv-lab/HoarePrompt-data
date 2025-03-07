#State of the program right berfore the function call: n and x are integers such that 1 ≤ x < n ≤ 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: `output1` contains all divisors of `x` that are less than or equal to the square root of `x`, and `output2` contains the corresponding divisors of `x` that are greater than the square root of `x`. The values of `n` and `x` remain unchanged.
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines `output2` and `output1`. `output1` contains all divisors of `x` that are less than or equal to the square root of `x` in reverse order, and `output2` contains the corresponding divisors of `x` that are greater than the square root of `x`.
#Overall this is what the function does:The function `func_1` accepts an integer `x` and returns a list containing all divisors of `x`. The list is structured such that the first part contains divisors of `x` that are greater than the square root of `x`, followed by the divisors that are less than or equal to the square root of `x` in reverse order. The values of `n` and `x` remain unchanged.

