#State of the program right berfore the function call: x and n are integers such that 1 ≤ x < n ≤ 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: `output1` contains all divisors of `x` ≤ `int(x
    output1.reverse()
    return output2 + output1
    #The program returns `output2` concatenated with `output1`, where `output1` contains all divisors of `x` ≤ `int(x)` in reverse order.
#Overall this is what the function does:The function accepts an integer `x` and returns a list of all divisors of `x`, sorted such that divisors greater than the square root of `x` appear first, followed by divisors less than or equal to the square root of `x` in descending order.

