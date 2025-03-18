#State of the program right berfore the function call: isOne is a boolean value, where if it is False, the function reads an integer from the input; if it is True, the function returns the integer 1.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer read from the input.
    else :
        return 1
        #The program returns 1
#Overall this is what the function does:The function accepts a boolean parameter `isOne`. If `isOne` is `False`, it reads an integer from the input and returns it. If `isOne` is `True`, it returns the integer 1.

#State of the program right berfore the function call: space is a boolean indicating whether the input line should be split into items based on spaces, and to_int is a boolean indicating whether the items should be converted to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: `space` and `to_int` are booleans, `line` is the input string. If `space` is True, `items` is a list of substrings from `line` split by spaces. If `space` is False, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers derived from `items`, where `items` is a list of substrings split by spaces if `space` is True, or a list of characters from `line` if `space` is False. Each element in `items` is converted to an integer.
    else :
        return items
        #The program returns `items`, which is a list of substrings from `line` split by spaces if `space` is True, or a list of characters from `line` if `space` is False. Since `to_int` is False, no conversion to integers occurs.
#Overall this is what the function does:The function reads a line of input and processes it based on two boolean parameters. If `space` is True, it splits the line into substrings separated by spaces; if `space` is False, it splits the line into individual characters. If `to_int` is True, each substring or character is converted to an integer. The function returns a list of these processed items, either as integers or strings.

#State of the program right berfore the function call: arr is a list of elements, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: `string` is the concatenation of all elements of `arr` (each converted to a string) with `sym` inserted between each element, and no trailing `sym`.
    return string
    #The program returns a string which is the concatenation of all elements of `arr` (each converted to a string) with `sym` inserted between each element, and no trailing `sym`.
#Overall this is what the function does:The function takes a list of elements (`arr`) and a string (`sym`), and returns a single string where each element of the list is converted to a string and concatenated together with `sym` inserted between each element, without a trailing `sym`.

#State of the program right berfore the function call: string is a string value, and substring is a string value.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: `string` is a string value, `substring` is a string value, `indices` is a list containing all starting indices of `substring` in `string`, `index` is -1.
    return indices
    #The program returns a list named `indices` which contains all starting indices of `substring` in `string`.
#Overall this is what the function does:The function takes two string inputs, `string` and `substring`, and returns a list of all starting indices where `substring` appears in `string`. If `substring` does not appear in `string`, the returned list will be empty.

#State of the program right berfore the function call: arr is a list of values, and element is a value of any type that may or may not be present in arr.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices from `arr` where the value matches `element`.
#Overall this is what the function does:The function takes a list `arr` and a value `element` as inputs and returns a list of indices where `element` is found in `arr`. If `element` is not present in `arr`, it returns an empty list.

#State of the program right berfore the function call: arr is a list of lists (2D list), index is a non-negative integer representing the column index to check within each sub-array, and value is a value that is being searched for in the specified column of each sub-array.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: None.
    return None
    #The program returns None
#Overall this is what the function does:The function searches through a 2D list `arr` for a sub-array where the element at the specified column index `index` matches the given `value`. If such a sub-array is found, it returns that sub-array; otherwise, it returns `None`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, start is an integer initialized to -1, end is a float initialized to 1000000000.0, num is a list that will store integers, t is an integer that can be 1, 2, or 3 representing the type of constraint, and v is an integer representing the value of the constraint.
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
        
    #State: `n` is an integer such that 2 <= n <= 100, `start` is the maximum value of `v` where `t == 1` encountered, `end` is the minimum value of `v` where `t == 2` encountered, `num` is a list of all `v` where `t == 3` encountered.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: `n` is an integer such that 2 <= n <= 100, `start` is the maximum value of `v` where `t == 1` encountered, `end` is the minimum value of `v` where `t == 2` encountered, `num` is a list of all `v` where `t == 3` encountered, and `count_num` is the number of elements in `num` that are within the range `[start, end]`.
    if (start > end) :
        return 0
        #The program returns 0
    #State: `n` is an integer such that 2 <= n <= 100, `start` is the maximum value of `v` where `t == 1` encountered, `end` is the minimum value of `v` where `t == 2` encountered, `num` is a list of all `v` where `t == 3` encountered, and `count_num` is the number of elements in `num` that are within the range `[start, end]`. Additionally, `start` is less than or equal to `end`.
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0
    #The program returns the value of `end - start + 1 - count_num` if `end - start + 1` is greater than or equal to `count_num`; otherwise, it returns 0.
#Overall this is what the function does:The function reads a series of constraints and values, determines a range based on specific constraints, and calculates how many additional numbers fall outside this range. It returns 0 if the range is invalid or if there are too many numbers inside the range; otherwise, it returns the count of numbers that can fit within the range without exceeding the given constraints.

