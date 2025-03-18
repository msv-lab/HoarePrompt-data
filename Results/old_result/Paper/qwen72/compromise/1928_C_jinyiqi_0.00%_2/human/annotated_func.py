#State of the program right berfore the function call: x is an integer such that 1 ≤ x ≤ 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: `x` is an integer such that 1 ≤ x ≤ 10^9, `output1` is a list containing all divisors of `x` that are less than or equal to the square root of `x`, and `output2` is a list containing the corresponding divisors of `x` that are greater than the square root of `x`, in decreasing order.
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines `output2` and `output1`. `output1` contains all divisors of `x` that are less than or equal to the square root of `x`, in reverse order. `output2` contains the corresponding divisors of `x` that are greater than the square root of `x`, in decreasing order. The resulting list is a combination of these two lists, with `output2` followed by `output1`.
#Overall this is what the function does:The function `func_1` accepts an integer `x` where 1 ≤ x ≤ 10^9 and returns a list of all divisors of `x`, sorted in decreasing order. The list includes both divisors that are less than or equal to the square root of `x` and those that are greater than the square root of `x`.

