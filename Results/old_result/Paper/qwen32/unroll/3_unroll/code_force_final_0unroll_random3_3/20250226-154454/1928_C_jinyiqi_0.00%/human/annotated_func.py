#State of the program right berfore the function call: x and n are integers such that 1 ≤ x < n ≤ 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: `x` and `n` are integers such that 1 ≤ x < n ≤ 10^9; `output1` is a list containing all divisors of `x` that are less than or equal to the square root of `x`; `output2` is a list containing the corresponding divisors of `x` that are greater than or equal to the square root of `x`, in descending order.
    output1.reverse()
    return output2 + output1
    #The program returns a list that first contains all divisors of `x` that are greater than or equal to the square root of `x` in descending order, followed by all divisors of `x` that are less than or equal to the square root of `x` in reversed order.
#Overall this is what the function does:The function accepts an integer `x` and returns a list of all divisors of `x`, first listing those that are greater than or equal to the square root of `x` in descending order, followed by those that are less than or equal to the square root of `x` in ascending order.

