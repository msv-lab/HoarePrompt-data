#State of the program right berfore the function call: x and n are integers such that 1 ≤ x < n ≤ 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: 
    output1.reverse()
    return output2 + output1
    #The program returns the concatenation of `output2` with the reversed version of its initial state `output1`.
#Overall this is what the function does:The function accepts an integer `x` and returns a list of integers that are the divisors of `x`, sorted such that larger divisors come before smaller divisors.

