#State of the program right berfore the function call: isOne is a boolean value.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value that is input by the user.
    else :
        return 1
        #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `False`, it prompts the user to input an integer and returns that integer. If `isOne` is `True`, it returns the integer 1.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input line by spaces, and to_int is a boolean indicating whether to convert the split items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *`space` is a boolean indicating whether to split the input line by spaces, `to_int` is a boolean indicating whether to convert the split items to integers, `line` is an input string. If `space` is `True`, `items` is a list of strings resulting from splitting `line` by spaces. If `space` is `False`, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers, where each integer is the result of converting the strings in `items` to integers. `items` is a list of strings resulting from splitting the input string `line` by spaces, since `space` is `True` and `to_int` is `True`.
    else :
        return items
        #The program returns a list of characters from the input string `line` since `space` is `False` and `to_int` is `False`.
#Overall this is what the function does:The function `func_2` accepts two boolean parameters, `space` and `to_int`. It reads an input string from the user. If `space` is `True`, it splits the input string by spaces into a list of substrings. If `space` is `False`, it converts the input string into a list of individual characters. If `to_int` is `True`, it converts each item in the list to an integer and returns the list of integers. If `to_int` is `False`, it returns the list of substrings or characters without conversion.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string used as a separator.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: Output State: `string` is a string containing all the integers from `arr` converted to strings, each followed by the separator `sym`. The last integer in `arr` is also followed by `sym`. The `arr` and `sym` variables remain unchanged.
    return string
    #The program returns a string containing all the integers from `arr` converted to strings, each followed by the separator `sym`. The last integer in `arr` is also followed by `sym`. The `arr` and `sym` variables remain unchanged.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a string `sym` as a separator. It returns a string where each integer from `arr` is converted to a string and followed by `sym`, including the last integer. The input parameters `arr` and `sym` remain unchanged after the function execution.

#State of the program right berfore the function call: string and substring are strings, where substring is a potential substring of string.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: `indices` contains all the starting indices of `substring` in `string`, and `index` is -1.
    return indices
    #The program returns the list `indices` which contains all the starting indices of `substring` in `string`.
#Overall this is what the function does:The function `func_4` accepts two parameters, `string` and `substring`, both of which are strings. It returns a list of integers, `indices`, which contains all the starting indices where `substring` is found within `string`. If `substring` is not found in `string`, the function returns an empty list. After the function concludes, the program state is such that `indices` contains all the starting indices of `substring` in `string`, and the variable `index` is -1.

#State of the program right berfore the function call: arr is a list of integers, and element is an integer.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices where the value in `arr` is equal to `element`.
#Overall this is what the function does:The function `func_5` accepts a list of integers `arr` and an integer `element`. It returns a list of indices where the value in `arr` is equal to `element`. If `element` is not found in `arr`, it returns an empty list.

#State of the program right berfore the function call: arr is a list of lists, index is a non-negative integer, and value is an integer.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: The loop returns the first subArray in arr where subArray[index] equals value, or it does not return anything (i.e., None) if no such subArray is found. The variables arr, index, and value remain unchanged.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_6` accepts a list of lists `arr`, a non-negative integer `index`, and an integer `value`. It returns the first sub-list in `arr` where the element at the specified `index` equals `value`. If no such sub-list is found, it returns `None`. The input parameters `arr`, `index`, and `value` remain unchanged.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100.
def func_7():
    n = int(input())
    start = -1
    end = 1000000000.0
    num = []
    for i in range(n):
        t, v = tuple(map(int, input().split()))
        
        if t == 1:
            if start < v:
                start = v
        
        if t == 2:
            if end > v:
                end = v
        
        if t == 3:
            num.append(v)
        
    #State: Output State: `n` is an input integer, `start` is the maximum value encountered for `t == 1`, `end` is the minimum value encountered for `t == 2`, `num` is a list containing all values encountered for `t == 3`.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: Output State: `n` is an input integer, `start` is the maximum value encountered for `t == 1`, `end` is the minimum value encountered for `t == 2`, `num` is a list containing all values encountered for `t == 3`, `count_num` is the number of elements in `num` that are between `start` and `end` (inclusive).
    if (start > end) :
        return 0
        #The program returns 0.
    #State: `n` is an input integer, `start` is the maximum value encountered for `t == 1`, `end` is the minimum value encountered for `t == 2`, `num` is a list containing all values encountered for `t == 3`, `count_num` is the number of elements in `num` that are between `start` and `end` (inclusive), and `start` is less than or equal to `end`.
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0
    #The program returns the difference between `end` and `start` plus 1, minus the number of elements in `num` that are between `start` and `end` (inclusive), if this difference is greater than or equal to the number of elements in `num` that are between `start` and `end` (inclusive). Otherwise, the program returns 0.
#Overall this is what the function does:The function `func_7` reads an integer `n` (where 2 <= n <= 100) and then reads `n` lines of input, each containing two integers `t` and `v`. It updates the `start` variable to the maximum value encountered for `t == 1`, the `end` variable to the minimum value encountered for `t == 2`, and appends values encountered for `t == 3` to a list `num`. After processing the inputs, the function calculates the number of elements in `num` that fall within the range `[start, end]` (inclusive). If `start` is greater than `end`, the function returns 0. Otherwise, it returns the difference between `end` and `start` plus 1, minus the count of elements in `num` within the range, but only if this difference is greater than or equal to the count. If the difference is less than the count, the function returns 0.

