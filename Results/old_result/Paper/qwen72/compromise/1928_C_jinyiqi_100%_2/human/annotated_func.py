#State of the program right berfore the function call: x is an integer such that 1 \le x \le 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: `x` is an integer such that 1 ≤ x ≤ 10^9, `output1` is a list containing all the divisors of `x` that are less than or equal to the square root of `x`. `output2` is a list containing the corresponding divisors of `x` that are greater than the square root of `x`, or equal to the square root if `x` is a perfect square.
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines all the divisors of `x` greater than or equal to the square root of `x` (from `output2`) with all the divisors of `x` less than or equal to the square root of `x` in reverse order (from `output1`). The resulting list contains all divisors of `x` in descending order.
#Overall this is what the function does:The function `func_1` accepts an integer `x` such that 1 ≤ x ≤ 10^9 and returns a list of all divisors of `x` in descending order. The list includes all integers that divide `x` without leaving a remainder, starting from the largest divisor down to 1. If `x` is a perfect square, the square root of `x` will appear only once in the list.

