#State of the program right berfore the function call: x and n are integers such that 1 <= x < n <= 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: The loop will continue to iterate as long as \(i\) (which starts from 2 and increments by 1 each iteration) is less than or equal to the square root of \(x\). After all iterations, `output1` will contain all divisors of `x` in ascending order, and `output2` will contain the corresponding quotients in descending order.
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines the quotients from the division of `x` by its divisors (in descending order) with the divisors themselves (also in descending order).
#Overall this is what the function does:The function `func_1` accepts an integer `x` and returns a list. This list contains the divisors of `x` in descending order, followed by their corresponding quotients when `x` is divided by these divisors, also in descending order.

