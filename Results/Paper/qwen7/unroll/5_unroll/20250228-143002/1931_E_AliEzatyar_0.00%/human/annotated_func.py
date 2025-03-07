#State of the program right berfore the function call: num is a list of integers where each integer is between 1 and 10^9 inclusive, and the length of num (n) is between 1 and 2 * 10^5 inclusive. Additionally, there are at most 10^4 test cases, and the parameter m is between 0 and 2 * 10^6 inclusive.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: counter is the number of zeros from the end of the list num until the first non-zero element.
    return counter
    #The program returns the number of zeros from the end of the list 'num' until the first non-zero element
#Overall this is what the function does:The function accepts a list of integers `num` and returns the count of zeros from the end of the list until the first non-zero element. If there are no zeros at the end, it returns zero.

