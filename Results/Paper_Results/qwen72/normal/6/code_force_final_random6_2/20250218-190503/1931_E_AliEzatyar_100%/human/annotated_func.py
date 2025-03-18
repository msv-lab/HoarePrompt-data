#State of the program right berfore the function call: num is a list of integers where 1 <= len(num) <= 2 * 10^5, and each integer a_i in num satisfies 1 <= a_i <= 10^9.
def func_1(num):
    counter = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '0':
            counter += 1
        else:
            break
        
    #State: The loop iterates from the last element to the first element of `num` in reverse order. The `counter` increments by 1 for each '0' encountered until a non-zero element is found or the loop reaches the beginning of the list. After all iterations, `counter` will be the number of trailing zeros in the list `num`, and `i` will be the index of the first non-zero element encountered from the end, or -1 if all elements are zero. The length of `num` remains unchanged, and each integer in `num` still satisfies 1 <= a_i <= 10^9.
    return counter
    #The program returns the number of trailing zeros in the list `num`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `num` and returns the number of trailing zeros in the list. The length of `num` remains unchanged, and the function does not modify the elements of the list. If the list contains no trailing zeros, the function returns 0. If the list is entirely composed of zeros, the function returns the length of the list.

