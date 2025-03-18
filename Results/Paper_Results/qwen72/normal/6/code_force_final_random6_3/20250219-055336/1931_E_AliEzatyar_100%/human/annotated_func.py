#State of the program right berfore the function call: num is a list of integers where each integer is in the range 1 to 10^9, and the length of num is an integer n such that 1 ≤ n ≤ 2 · 10^5. Additionally, there is an integer m (0 ≤ m ≤ 2 · 10^6) that determines the winning condition for Sasha.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: `num` is a list of integers where each integer is in the range 1 to 10^9, and the length of `num` is an integer `n` such that 1 ≤ n ≤ 2 · 10^5, `m` is an integer (0 ≤ m ≤ 2 · 10^6), `i` is -1. `counter` is the number of trailing '0's in the list `num` up to the first non-'0' element, or 0 if there are no trailing '0's.
    return counter
    #The program returns the number of trailing '0's in the list `num` up to the first non-'0' element, or 0 if there are no trailing '0's.
#Overall this is what the function does:The function `func_1` accepts a list of integers `num` and returns the number of trailing zeros in the list, counting from the end of the list until the first non-zero element is encountered. If there are no trailing zeros, the function returns 0.

