#State of the program right berfore the function call: arr is a list of non-negative integers, and x is a non-negative integer such that 0 <= x < 2^30.
def func_1(arr, x):
    return find_max(arr, 31)
    #The program returns the maximum value in the list 'arr' considering 31 bits.
#Overall this is what the function does:The function accepts a list of non-negative integers `arr` and a non-negative integer `x`. It returns the maximum value present in the list `arr` when considering each element as a 31-bit unsigned integer.

#State of the program right berfore the function call: cur_arr is a list of non-negative integers representing a subarray of the original array a, bit is an integer representing the current bit position being considered (starting from the most significant bit to the least significant bit), and x is an integer representing the favorite number of Yarik.
def find_max(cur_arr, bit):
    if (bit == -1) :
        return len(cur_arr)
        #The program returns the length of the list 'cur_arr'
    #State: cur_arr is a list of non-negative integers representing a subarray of the original array a, bit is an integer representing the current bit position being considered (starting from the most significant bit to the least significant bit), and x is an integer representing the favorite number of Yarik. The value of bit is not -1.
    new_arr = []
    xor = 0
    thing1 = 0
    for i in cur_arr:
        xor ^= i
        
        if not xor >> bit & 1:
            new_arr.append(xor)
            xor = 0
        
    #State: Output State: `cur_arr` is a list of non-negative integers representing a subarray of the original array `a`, `bit` is an integer representing the current bit position being considered (starting from the most significant bit to the least significant bit), `x` is an integer representing the favorite number of Yarik, `new_arr` is a list containing elements where each element is the cumulative XOR of subarrays of `cur_arr` whose XOR value in the current bit position is 0, `xor` is 0, `thing1` is 0.
    if (xor >> bit & 1) :
        thing1 = -1
    else :
        thing1 = find_max(new_arr, bit - 1)
    #State: `cur_arr` is a list of non-negative integers representing a subarray of the original array `a`, `bit` is an integer representing the current bit position being considered, `x` is an integer representing the favorite number of Yarik, `new_arr` is a list containing elements where each element is the cumulative XOR of subarrays of `cur_arr` whose XOR value in the current bit position matches the value of the current bit of `xor`, `xor` is 0, and `thing1` is either -1 or the result of the function `find_max(new_arr, bit - 1)` depending on whether the current bit of `xor` is 1 or 0.
    if (x >> bit & 1) :
        return max(find_max(cur_arr, bit - 1), len(new_arr))
        #The program returns the maximum value between the result of find_max(cur_arr, bit - 1) and the length of new_arr.
    else :
        return thing1
        #The program returns either -1 or the result of the function find_max(new_arr, bit - 1) depending on whether the current bit of xor is 0 or 1.
#Overall this is what the function does:The function `find_max` takes a list of non-negative integers `cur_arr` and an integer `bit` as input. It processes the list based on the current bit position and returns either the length of `cur_arr`, the maximum value between the result of another call to `find_max` with the previous bit position and the length of a new list, or -1, depending on the current bit and the intermediate results.

