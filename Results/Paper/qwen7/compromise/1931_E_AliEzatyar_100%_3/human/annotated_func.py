#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: The output state after the loop executes all the iterations is that `counter` will be equal to the number of trailing zeros in the string representation of `num`, and `i` will be less than or equal to -1.
    return counter
    #The program returns the number of trailing zeros in the string representation of num.
#Overall this is what the function does:The function accepts an integer num (where 1 ≤ num ≤ 10^9) and returns the count of trailing zeros in its string representation. It iterates through the string representation of num from the end to the beginning, counting the number of consecutive '0' characters until it encounters a non-zero character or reaches the start of the string.

