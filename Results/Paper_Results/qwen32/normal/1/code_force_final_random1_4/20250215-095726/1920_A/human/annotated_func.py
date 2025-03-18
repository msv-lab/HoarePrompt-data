#State of the program right berfore the function call: isOne is a boolean value indicating whether to return 1 or take an integer input from the user.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer input from the user
    else :
        return 1
        #The program returns 1
#Overall this is what the function does:The function accepts a boolean parameter `isOne`. If `isOne` is `True`, it returns 1. If `isOne` is `False`, it returns an integer input from the user.

#State of the program right berfore the function call: space is a boolean indicating whether the input line should be split into multiple items, and to_int is a boolean indicating whether the items should be converted to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: `space` is a boolean indicating whether the input line should be split into multiple items, and `to_int` is a boolean indicating whether the items should be converted to integers; `line` is the input string provided by the user. If `space` is True, `items` is a list of substrings from `line` split by whitespace. If `space` is False, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers where each integer is derived from converting each item in the list `items` to an integer. Since `to_int` is True, every element in `items` (which is either a list of substrings split by whitespace if `space` is True, or a list of characters if `space` is False) is converted to an integer.
    else :
        return items
        #The program returns `items`, which is a list of characters from `line` since `space` is False.
#Overall this is what the function does:The function reads a line of input from the user and processes it based on the values of the `space` and `to_int` parameters. If `space` is `True`, the input line is split into substrings separated by whitespace; otherwise, it is split into individual characters. If `to_int` is `True`, each substring or character is converted to an integer. The function returns a list of these processed items.

#State of the program right berfore the function call: arr is a list of elements and sym is a string symbol used to concatenate the string representations of the elements in arr.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: a concatenation of the string representations of all elements in `arr`, each followed by `sym`, except no trailing `sym` at the end.
    return string
    #The program returns the string which is a concatenation of the string representations of all elements in `arr`, each followed by `sym`, except no trailing `sym` at the end.
#Overall this is what the function does:The function takes a list of elements and a string symbol, then returns a single string that concatenates the string representations of the elements in the list, each followed by the symbol, without a trailing symbol.

#State of the program right berfore the function call: string is a string, and substring is a string.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: `string` is a string, `substring` is a string, `indices` is a list containing all the starting indices of each occurrence of `substring` in `string`, `index` is `-1`.
    return indices
    #The program returns a list `indices` containing all the starting indices of each occurrence of `substring` in `string`.
#Overall this is what the function does:The function takes two string inputs, `string` and `substring`, and returns a list of all starting indices where `substring` occurs within `string`. If `substring` is not found, it returns an empty list.

#State of the program right berfore the function call: arr is a list of elements, and element is a value that may or may not be present in arr.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices from the list `arr` where the value matches `element`.
#Overall this is what the function does:The function takes a list `arr` and a value `element`, and returns a list of indices where `element` is found in `arr`. If `element` is not present in `arr`, it returns an empty list.

#State of the program right berfore the function call: arr is a list of lists (subArrays), index is a non-negative integer representing the index within each subArray, and value is a value that could be present at the specified index in any of the subArrays.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: None
    return None
    #The program returns None
#Overall this is what the function does:The function `func_6` accepts a list of lists (`arr`), a non-negative integer (`index`), and a value (`value`). It returns a subArray from `arr` where the element at `index` is equal to `value` if such a subArray exists. If no such subArray exists, it returns `None`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, start is an integer initialized to -1, end is a float initialized to 1000000000.0, num is a list that will store integers. t is an integer that represents the type of constraint (1, 2, or 3), and v is an integer representing the value associated with the constraint.
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
        
    #State: `start` is the highest `v` when `t` is 1, `end` is the lowest `v` when `t` is 2, and `num` contains all `v` when `t` is 3.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: `start` is the highest `v` when `t` is 1, `end` is the lowest `v` when `t` is 2, `num` contains all `v` when `t` is 3, and `count_num` is the number of elements in `num` that are between `start` and `end` inclusive.
    if (start > end) :
        return 0
        #The program returns 0
    #State: `start` is the highest `v` when `t` is 1, `end` is the lowest `v` when `t` is 2, `num` contains all `v` when `t` is 3, and `count_num` is the number of elements in `num` that are between `start` and `end` inclusive. Additionally, `start` is less than or equal to `end`.
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0
    #The program returns the value of `end - start + 1 - count_num` if `end - start + 1` is greater than or equal to `count_num`; otherwise, it returns 0.
#Overall this is what the function does:The function reads a series of constraints and values, then calculates and returns the number of integers within a specified range that do not match any given values. If the range is invalid (start greater than end), it returns 0.

