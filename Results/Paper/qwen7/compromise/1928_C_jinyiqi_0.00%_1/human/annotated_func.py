#State of the program right berfore the function call: x and n are integers such that 1 <= x < n <= 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: After the loop executes all iterations, `output1` contains all divisors of `x` in ascending order, and `output2` contains the corresponding quotients in descending order.
    output1.reverse()
    return output2 + output1
    #The program returns a list that combines the divisors of x in descending order (from `output1`) with the corresponding quotients in descending order (from `output2`).
#Overall this is what the function does:The function accepts an integer \( x \) and returns a list containing the divisors of \( x \) in descending order, followed by the corresponding quotients in descending order.

