#State of the program right berfore the function call: isOne is a boolean value.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value input by the user.
    else :
        return 1
        #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `True`, it returns the integer value `1`. If `isOne` is `False`, it prompts the user to input an integer and returns that integer value.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input line by spaces, to_int is a boolean indicating whether to convert the split items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *`space` is a boolean indicating whether to split the input line by spaces, `to_int` is a boolean indicating whether to convert the split items to integers, `line` is the input string. If `space` is true, `items` is a list of strings resulting from splitting `line` by spaces. If `space` is false, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers, where each integer is the result of converting the items in the `items` list to integers. The `items` list is derived from splitting the `line` string by spaces, since `space` is true and `to_int` is true.
    else :
        return items
        #The program returns a list of characters from the input string `line` if `space` is false. If `space` is true, it returns a list of strings resulting from splitting `line` by spaces. Since `to_int` is false, the items are not converted to integers.
#Overall this is what the function does:The function `func_2` accepts two boolean parameters: `space` and `to_int`. It reads a line of input from the user. If `space` is true, it splits the input line into a list of strings based on spaces. If `space` is false, it converts the input line into a list of individual characters. If `to_int` is true, it converts each item in the list to an integer and returns a list of integers. If `to_int` is false, it returns the list of strings or characters as is, depending on the value of `space`.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string used as a separator.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: Output State: `string` is a string containing all the integers from the list `arr` converted to strings, concatenated together, with the string `sym` used as a separator between each integer. The list `arr` and the string `sym` remain unchanged.
    return string
    #The program returns a string containing all the integers from the list `arr` converted to strings, concatenated together, with the string `sym` used as a separator between each integer. The list `arr` and the string `sym` remain unchanged.
#Overall this is what the function does:The function `func_3` takes a list of integers `arr` and a string `sym` as parameters. It returns a string where each integer from `arr` is converted to a string and concatenated together, with `sym` used as a separator between each integer. The original list `arr` and the string `sym` remain unchanged.

#State of the program right berfore the function call: string and substring are strings, where substring is a sequence of characters that may or may not be present in string.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: `indices` is a list containing all the starting positions of `substring` in `string`, and `index` is -1.
    return indices
    #The program returns a list containing all the starting positions of `substring` in `string`.
#Overall this is what the function does:The function `func_4` accepts two parameters, `string` and `substring`, both of which are strings. It returns a list of all the starting positions (indices) where `substring` is found within `string`. If `substring` is not found in `string`, the function returns an empty list.

#State of the program right berfore the function call: arr is a list of integers, and element is an integer.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices where the value in the list `arr` is equal to the integer `element`.
#Overall this is what the function does:The function `func_5` accepts a list of integers `arr` and an integer `element`. It returns a list of indices where the value in `arr` is equal to `element`. If no such elements are found, it returns an empty list. The function does not modify the input list `arr`.

#State of the program right berfore the function call: arr is a list of lists, index is a non-negative integer, and value is an integer.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: The loop will return the first subArray in arr where subArray[index] equals value. If no such subArray is found, the loop will not return any subArray and the function will implicitly return None. The variables arr, index, and value remain unchanged.
    return None
    #The program returns None.
#Overall this is what the function does:The function `func_6` accepts a list of lists `arr`, a non-negative integer `index`, and an integer `value`. It searches through the list `arr` and returns the first sub-list where the element at the specified `index` equals `value`. If no such sub-list is found, the function returns `None`. The input variables `arr`, `index`, and `value` remain unchanged.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, start is an integer initialized to -1, end is a float initialized to 1000000000.0, num is an empty list.
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
        
    #State: Output State: `n` is an integer input by the user, `start` is the highest value of `v` for which `t` was 1, `end` is the lowest value of `v` for which `t` was 2, `num` is a list containing all values of `v` for which `t` was 3. If no `t` was 1, `start` remains -1. If no `t` was 2, `end` remains 1000000000.0. If no `t` was 3, `num` remains an empty list.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: `n` remains unchanged, `start` remains unchanged, `end` remains unchanged, `num` remains unchanged, `count_num` is the number of elements in `num` that are between `start` and `end` (inclusive).
    if (start > end) :
        return 0
        #The program returns 0.
    #State: *`n` remains unchanged, `start` remains unchanged, `end` remains unchanged, `num` remains unchanged, `count_num` is the number of elements in `num` that are between `start` and `end` (inclusive), and `start` is less than or equal to `end`
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0
    #The program returns 0 if the number of elements in `num` that are between `start` and `end` (inclusive) is greater than or equal to the range `end - start + 1`. Otherwise, it returns the difference `end - start + 1 - count_num`.
#Overall this is what the function does:The function `func_7` reads an integer `n` from the user and then reads `n` pairs of integers `(t, v)`. It updates `start` to the highest value of `v` where `t` is 1, `end` to the lowest value of `v` where `t` is 2, and appends `v` to the list `num` where `t` is 3. After processing all pairs, the function returns 0 if `start` is greater than `end`. Otherwise, it returns 0 if the number of elements in `num` that are between `start` and `end` (inclusive) is greater than or equal to the range `end - start + 1`. If neither condition is met, it returns the difference `end - start + 1 - count_num`. The function does not modify `n`, `start`, `end`, or `num` after the initial processing.

