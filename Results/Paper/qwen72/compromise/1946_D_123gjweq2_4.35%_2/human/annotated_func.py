#State of the program right berfore the function call: arr is a list of integers where 0 <= arr[i] < 2^30 for all i, and x is an integer such that 0 <= x < 2^30.
def func_1(arr, x):
    return find_max(arr, 31)
    #The program returns the maximum integer value found in the list `arr`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and an integer `x`. It returns the maximum integer value found in the list `arr`. The parameter `x` is not used within the function. After the function concludes, the list `arr` remains unchanged, and the maximum value from `arr` is returned.

#State of the program right berfore the function call: cur_arr is a list of integers where 0 <= cur_arr[i] < 2^30 for all i, and bit is an integer such that 0 <= bit < 30.
def find_max(cur_arr, bit):
    if (bit == -1) :
        return len(cur_arr)
        #The program returns the number of integers in the list `cur_arr`.
    #State: cur_arr is a list of integers where 0 <= cur_arr[i] < 2^30 for all i, and bit is an integer such that 0 <= bit < 30, and bit is not equal to -1.
    new_arr = []
    xor = 0
    thing1 = 0
    for i in cur_arr:
        xor ^= i
        
        if not xor >> bit & 1:
            new_arr.append(xor)
            xor = 0
        
    #State: new_arr is a list of integers where each element is the cumulative XOR of elements in cur_arr until the bit position specified by bit is 0, xor is 0, and thing1 is 0.
    if (xor >> bit & 1) :
        thing1 = -1
    else :
        thing1 = find_max(new_arr, bit - 1)
    #State: *new_arr is a list of integers where each element is the cumulative XOR of elements in cur_arr until the bit position specified by bit is 0, and `xor` is 0. If the bit at position `bit` in `xor` is 1, `thing1` is -1. Otherwise, if the bit at position `bit` in `xor` is 0, `thing1` is the result of `find_max(new_arr, bit - 1)`.
    if (x >> bit & 1) :
        return max(find_max(cur_arr, bit - 1), len(new_arr))
        #The program returns the maximum value between the result of `find_max(cur_arr, bit - 1)` and the length of `new_arr`.
    else :
        return thing1
        #The program returns -1 or the result of `find_max(new_arr, bit - 1)`, depending on whether the bit at position `bit` in `xor` is 1 or 0.
#Overall this is what the function does:The function `find_max` accepts a list of integers `cur_arr` and an integer `bit`. It returns the number of integers in `cur_arr` if `bit` is -1. Otherwise, it processes the list to create a new list `new_arr` where each element is the cumulative XOR of elements in `cur_arr` until the bit position specified by `bit` is 0. If the bit at position `bit` in the cumulative XOR of `cur_arr` is 1, it returns the maximum value between the result of `find_max(cur_arr, bit - 1)` and the length of `new_arr`. If the bit at position `bit` in the cumulative XOR of `cur_arr` is 0, it returns the result of `find_max(new_arr, bit - 1)`. If the bit at position `bit` in the cumulative XOR of `cur_arr` is 1 and `new_arr` is not processed, it returns -1.

