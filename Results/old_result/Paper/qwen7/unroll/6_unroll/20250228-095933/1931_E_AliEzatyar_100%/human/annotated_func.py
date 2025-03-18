#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: Output State: `counter` is the number of trailing zeros in the binary representation of `num`.
    return counter
    #The program returns the number of trailing zeros in the binary representation of num
#Overall this is what the function does:The function accepts an integer `num` between 1 and 10^9 and returns the number of trailing zeros in its binary representation.

