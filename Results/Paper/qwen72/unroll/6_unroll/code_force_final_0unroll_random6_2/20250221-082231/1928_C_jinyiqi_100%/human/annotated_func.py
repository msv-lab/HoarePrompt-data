#State of the program right berfore the function call: x is an integer such that 1 \le x \le 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: `output1` contains all divisors of `x` that are less than or equal to the square root of `x`, and `output2` contains the corresponding divisors of `x` that are greater than the square root of `x`.
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines `output2` (containing divisors of `x` that are greater than the square root of `x`) and `output1` (containing divisors of `x` that are less than or equal to the square root of `x`, in reversed order).
#Overall this is what the function does:The function `func_1` accepts an integer `x` (where 1 ≤ x ≤ 10^9) and returns a list containing all divisors of `x`. The divisors are ordered such that those greater than the square root of `x` appear first, followed by those less than or equal to the square root of `x` in reversed order.

