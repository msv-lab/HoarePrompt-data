#State of the program right berfore the function call: x is an integer such that 1 ≤ x ≤ 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: `x` is an integer such that 1 ≤ x ≤ 10^9, `output1` is a list of all divisors of `x` that are less than or equal to the square root of `x`, `output2` is a list of the corresponding divisors of `x` that are greater than the square root of `x` (or equal if `x` is a perfect square).
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines all divisors of `x` that are greater than the square root of `x` (or equal if `x` is a perfect square) with all divisors of `x` that are less than or equal to the square root of `x` in reverse order.
#Overall this is what the function does:The function `func_1` accepts an integer `x` (1 ≤ x ≤ 10^9) and returns a list containing all divisors of `x` that are greater than or equal to the square root of `x`, followed by all divisors of `x` that are less than or equal to the square root of `x` in reverse order. The input `x` remains unchanged.

