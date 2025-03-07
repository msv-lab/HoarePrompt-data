#State of the program right berfore the function call: x is an integer such that 1 \le x < n \le 10^9, where n is Vasya's position in the line.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: `output1` contains all divisors of `x` that are less than or equal to the square root of `x`, and `output2` contains their corresponding complementary divisors (i.e., `x` divided by each divisor in `output1`). The variable `x` remains unchanged.
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines `output2` and `output1`. `output1` contains all divisors of `x` that are less than or equal to the square root of `x` in reverse order, and `output2` contains their corresponding complementary divisors.
#Overall this is what the function does:The function `func_1` accepts an integer `x` and returns a list containing all divisors of `x` that are less than or equal to the square root of `x` in reverse order, followed by their corresponding complementary divisors. The input variable `x` remains unchanged.

