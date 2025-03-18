#State of the program right berfore the function call: x and n are integers such that 1 <= x < n <= 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: Postcondition: `x` is an integer such that \(1 \leq x < n \leq 10^9\), `i` is the largest integer such that \(i^2 \leq x\), `output1` is a list containing all divisors of `x` that are less than or equal to \(\sqrt{x}\), and `output2` is a list containing the corresponding quotients of `x` divided by each divisor in `output1` in the same order.
    output1.reverse()
    return output2 + output1
    #The program returns a list that is the concatenation of `output2` (list of quotients) and `output1` (list of divisors of `x` that are less than or equal to \(\sqrt{x}\) in descending order)
#Overall this is what the function does:The function accepts an integer `x` and returns a list. This list contains all divisors of `x` that are less than or equal to \(\sqrt{x}\) in descending order, followed by their corresponding quotients when `x` is divided by these divisors.

