#State of the program right berfore the function call: isOne is a boolean value (True or False).
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value that is input by the user.
    else :
        return 1
        #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is True, the function returns the integer value 1. If `isOne` is False, the function prompts the user to input an integer and returns that integer.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input line by spaces, to_int is a boolean indicating whether to convert the split items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *`line` is the input string, `space` is a boolean indicating whether to split the input line by spaces, `to_int` is a boolean indicating whether to convert the split items to integers. If `space` is `True`, `items` is a list of strings resulting from splitting `line` by spaces. If `space` is `False`, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers where each integer is the result of converting the items in the `items` list to integers. The `items` list is derived from splitting the input string `line` by spaces since `space` is `True` and `to_int` is `True`.
    else :
        return items
        #The program returns a list of characters from the input string `line`.
#Overall this is what the function does:The function `func_2` accepts two boolean parameters, `space` and `to_int`. It reads an input string from the user. If `space` is `True`, it splits the string into a list of substrings based on spaces. If `space` is `False`, it converts the string into a list of individual characters. If `to_int` is `True`, it converts each element of the resulting list into an integer and returns the list of integers. If `to_int` is `False`, it returns the list of substrings or characters directly.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string used as a separator.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: Output State: `string` is a string containing all the integers from the list `arr` converted to strings, each followed by the separator `sym`. The final character in `string` will be `sym` if `arr` is not empty. The list `arr` and the string `sym` remain unchanged.
    return string
    #The program returns a string containing all the integers from the list `arr` converted to strings, each followed by the separator `sym`. If `arr` is not empty, the final character in the returned string will be `sym`. The list `arr` and the string `sym` remain unchanged.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a string `sym`. It returns a string where each integer in `arr` is converted to a string and concatenated with `sym`. If `arr` is not empty, the final character in the returned string will be `sym`. The original list `arr` and the string `sym` remain unchanged.

#State of the program right berfore the function call: string is a string, and substring is a string that may or may not be present in string.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: indices is a list containing all the starting indices of occurrences of substring in string, and index is -1.
    return indices
    #The program returns the list 'indices' which contains all the starting indices of occurrences of a substring in a string.
#Overall this is what the function does:The function `func_4` accepts two parameters, `string` and `substring`, both of which are strings. It returns a list of integers representing the starting indices of all occurrences of `substring` within `string`. If `substring` is not found in `string`, the function returns an empty list. The original `string` and `substring` remain unchanged.

#State of the program right berfore the function call: arr is a list of integers, and element is an integer.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices where the value in `arr` is equal to `element`.
#Overall this is what the function does:The function `func_5` accepts a list of integers `arr` and an integer `element`. It returns a list of indices where the value in `arr` is equal to `element`. If `element` is not found in `arr`, the function returns an empty list. The function does not modify the input list `arr`.

#State of the program right berfore the function call: arr is a list of lists where each sub-list contains at least `index + 1` elements, index is a non-negative integer, and value is an integer.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: The loop will either return the first sub-list in `arr` where the element at the specified `index` is equal to `value`, or it will not return anything and the loop will complete all iterations. The state of `arr`, `index`, and `value` remains unchanged.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_6` accepts a list of lists `arr`, a non-negative integer `index`, and an integer `value`. It searches through `arr` for the first sub-list where the element at the specified `index` is equal to `value`. If such a sub-list is found, it returns that sub-list. If no such sub-list is found, it returns `None`. The state of `arr`, `index`, and `value` remains unchanged after the function concludes.

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
        
    #State: Output State: `n` is an integer input by the user, and 2 <= n <= 100; `start` is the maximum value of `v` for all `t == 1` inputs, or -1 if no such input exists; `end` is the minimum value of `v` for all `t == 2` inputs, or 1000000000.0 if no such input exists; `num` is a list containing all `v` values for which `t == 3`.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: Output State: `count_num` is the number of elements in `num` that are greater than or equal to `start` and less than or equal to `end`. The values of `n`, `start`, and `end` remain unchanged. `num` remains the same list of values.
    if (start > end) :
        return 0
        #The program returns 0.
    #State: `count_num` is the number of elements in `num` that are greater than or equal to `start` and less than or equal to `end`. The values of `n`, `start`, and `end` remain unchanged. `num` remains the same list of values. `start` is less than or equal to `end`.
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0
    #The program returns the difference between `end - start + 1` and `count_num` if `end - start + 1` is greater than or equal to `count_num`. Otherwise, the program returns 0. `end - start + 1` is the total number of integers in the range from `start` to `end` (inclusive), and `count_num` is the number of elements in `num` that fall within this range.
#Overall this is what the function does:The function `func_7` reads an integer `n` from user input, where `2 <= n <= 100`. It then processes `n` pairs of integers `(t, v)`. Based on the value of `t`, it updates `start` to the maximum `v` for `t == 1`, `end` to the minimum `v` for `t == 2`, and appends `v` to a list `num` for `t == 3`. After processing, it counts the number of elements in `num` that fall within the range `[start, end]` (inclusive). If `start` is greater than `end`, the function returns 0. Otherwise, it returns the difference between the total number of integers in the range `[start, end]` and the count of elements in `num` that fall within this range, provided the total number of integers in the range is greater than or equal to the count. If this condition is not met, it returns 0. The values of `n`, `start`, `end`, and `num` remain unchanged after the function concludes.

