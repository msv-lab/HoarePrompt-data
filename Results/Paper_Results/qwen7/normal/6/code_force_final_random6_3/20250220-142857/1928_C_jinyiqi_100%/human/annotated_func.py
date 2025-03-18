#State of the program right berfore the function call: x and n are integers such that 1 <= x < n <= 10^9.
def func_1(x):
    output1 = []
    output2 = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            output1.append(i)
            output2.append(int(x / i))
        
    #State: The loop will continue to iterate as long as `i` (which starts from 2 and increments by 1 each iteration) is less than or equal to the square root of `x`. Once `i` exceeds the square root of `x`, the loop will terminate. `output1` will contain all divisors of `x` starting from 1 up to the largest divisor less than or equal to the square root of `x`. `output2` will contain the corresponding quotients for each divisor in `output1`.
    output1.reverse()
    return output2 + output1
    #The program returns a string that is the concatenation of 'output2' followed by the reversed version of 'output1'
#Overall this is what the function does:The function accepts an integer \( x \) and returns a string. This string is formed by first listing the quotients of all divisors of \( x \) that are greater than or equal to the square root of \( x \), followed by the reverse order of all divisors of \( x \) that are less than the square root of \( x \).

