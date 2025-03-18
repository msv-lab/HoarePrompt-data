#State of the program right berfore the function call: num is a list of integers where each integer is in the range 1 to 10^9, and the length of num is in the range 1 to 2 * 10^5.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `num` is a list of integers where each integer is in the range 1 to 10^9, and the length of `num` is in the range 1 to 2 * 10^5; `counter` is the number of trailing zeros in `num`, and `i` is the index of the first non-zero element from the end of the list, or -1 if all elements are zero.
    return counter
    #The program returns the number of trailing zeros in the list `num`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `num` and returns the number of trailing zeros in the list. The list `num` remains unchanged after the function call.

