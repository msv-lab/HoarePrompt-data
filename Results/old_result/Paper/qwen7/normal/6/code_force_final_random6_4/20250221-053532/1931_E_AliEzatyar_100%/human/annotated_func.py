#State of the program right berfore the function call: num is an integer such that 1 <= num <= 10^9.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: counter is a value between 0 and the length of num (inclusive), and num is an integer such that \(1 \leq \text{num} \leq 10^9\).
    return counter
    #The program returns the value of counter, which is a value between 0 and the length of num (inclusive)
#Overall this is what the function does:The function accepts an integer num within the range of 1 to 10^9. It counts the number of trailing zeros in the string representation of num and returns this count as an integer. If num does not contain any trailing zeros, it returns 0.

