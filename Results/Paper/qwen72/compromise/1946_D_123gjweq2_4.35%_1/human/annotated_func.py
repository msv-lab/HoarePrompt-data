#State of the program right berfore the function call: arr is a list of integers where 0 <= arr[i] < 2^30 for all i, and x is an integer such that 0 <= x < 2^30.
def func_1(arr, x):
    return find_max(arr, 31)
    #The program returns the maximum integer value from the list `arr`.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers and an integer `x`, but it does not use `x` in its execution. The function returns the maximum integer value from the list `arr`. The state of the program after the function concludes is that the maximum value from `arr` is returned, and `x` remains unchanged.

#State of the program right berfore the function call: cur_arr is a list of non-negative integers, and bit is a non-negative integer such that 0 <= bit < 30.
def find_max(cur_arr, bit):
    if (bit == -1) :
        return len(cur_arr)
        #The program returns the length of the list `cur_arr`.
    #State: cur_arr is a list of non-negative integers, and bit is a non-negative integer such that 0 <= bit < 30, and bit is not equal to -1.
    new_arr = []
    xor = 0
    thing1 = 0
    for i in cur_arr:
        xor ^= i
        
        if not xor >> bit & 1:
            new_arr.append(xor)
            xor = 0
        
    #State: new_arr is a list of non-negative integers where each element is the cumulative XOR of elements in cur_arr up to the point where the bit-th bit of the cumulative XOR is 0, xor is 0, thing1 remains 0.
    if (xor >> bit & 1) :
        thing1 = -1
    else :
        thing1 = find_max(new_arr, bit - 1)
    #State: *new_arr is a list of non-negative integers where each element is the cumulative XOR of elements in cur_arr up to the point where the bit-th bit of the cumulative XOR is 0, xor is 0. If the bit-th bit of the current value of xor is 1, `thing1` is -1. Otherwise, the bit-th bit of xor is 0, and `thing1` is the result of `find_max(new_arr, bit - 1)`.
    if (x >> bit & 1) :
        return max(find_max(cur_arr, bit - 1), len(new_arr))
        #The program returns the maximum value between the result of the function `find_max(cur_arr, bit - 1)` and the length of the list `new_arr`.
    else :
        return thing1
        #The program returns -1 or the result of `find_max(new_arr, bit - 1)`, depending on whether the bit-th bit of `xor` is 1 or 0.
#Overall this is what the function does:The function `find_max` accepts a list of non-negative integers `cur_arr` and a non-negative integer `bit` (0 <= bit < 30). It returns the length of `cur_arr` if `bit` is -1. Otherwise, it processes `cur_arr` to create a new list `new_arr` containing cumulative XOR values of elements in `cur_arr` up to the point where the bit-th bit of the cumulative XOR is 0. If the bit-th bit of the final cumulative XOR is 1, it returns the maximum value between the result of `find_max(cur_arr, bit - 1)` and the length of `new_arr`. If the bit-th bit of the final cumulative XOR is 0, it returns the result of `find_max(new_arr, bit - 1)`. If `new_arr` is empty and the bit-th bit of the final cumulative XOR is 0, it returns -1.

