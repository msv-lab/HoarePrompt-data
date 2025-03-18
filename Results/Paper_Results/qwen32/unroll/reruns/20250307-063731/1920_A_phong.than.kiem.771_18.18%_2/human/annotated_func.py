#State of the program right berfore the function call: isOne is a boolean value, where if it is False, the function reads and returns an integer from the input, and if it is True, the function returns the integer 1.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer read from the input.
    else :
        return 1
        #The program returns 1
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `False`, it reads an integer from the input and returns it. If `isOne` is `True`, it returns the integer 1.

#State of the program right berfore the function call: space is a boolean indicating whether the input line should be split into items based on spaces, and to_int is a boolean indicating whether the resulting items should be converted to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: `space` is a boolean, `to_int` is a boolean, `line` is the input string. If `space` is True, `items` is a list of substrings from `line` split by spaces. If `space` is False, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers where each integer is the result of converting each element in `items` to an integer. If `space` is True, `items` contains substrings from `line` split by spaces. If `space` is False, `items` contains individual characters from `line`. Since `to_int` is True, each element in `items` is converted to an integer before being included in the returned list.
    else :
        return items
        #The program returns `items`, which is a list of substrings from `line` split by spaces if `space` is True, or a list of characters from `line` if `space` is False. Since `to_int` is False, no conversion to integers occurs.
#Overall this is what the function does:The function reads a line of input and returns a list of items derived from that line. If `space` is True, the line is split into substrings based on spaces; if `space` is False, the line is split into individual characters. If `to_int` is True, each item in the list is converted to an integer. If `to_int` is False, the items are returned as strings.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: `arr` is a list of integers, `sym` is a string, `string` is a concatenation of all integers in `arr` with `sym` appended after each integer except the last one.
    return string
    #The program returns a string that is a concatenation of all integers in the list `arr` with the string `sym` appended after each integer except the last one.
#Overall this is what the function does:The function takes a list of integers and a string as input, and returns a single string that is the concatenation of the integers from the list, with the given string appended after each integer except the last one.

#State of the program right berfore the function call: string is a string, and substring is a string.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: `indices` contains all starting indices of `substring` in `string`, and `index` is `-1`.
    return indices
    #The program returns `indices` which contains all starting indices of `substring` in `string`.
#Overall this is what the function does:The function accepts two string parameters, `string` and `substring`. It returns a list of all starting indices where `substring` is found within `string`. If `substring` is not found, it returns an empty list.

#State of the program right berfore the function call: arr is a list of elements, and element is a value that can be present in the list arr.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices where the value 'element' is found in the list 'arr'.
#Overall this is what the function does:The function accepts a list `arr` and a value `element`. It returns a list of all indices where the value `element` is found in the list `arr`. If the `element` is not present in the list, it returns an empty list.

#State of the program right berfore the function call: arr is a list of lists, index is a non-negative integer, and value is a value of any type.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: arr is a list of lists, index is a non-negative integer, and value is a value of any type. The function returns None.
    return None
    #The program returns None.
#Overall this is what the function does:The function accepts a list of lists (`arr`), a non-negative integer (`index`), and a value (`value`). It searches through each sublist in `arr` to find a sublist where the element at the position specified by `index` matches the given `value`. If such a sublist is found, it returns that sublist. If no matching sublist is found after checking all sublists, the function returns `None`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100, start is an integer initialized to -1, end is a float initialized to 1000000000.0, num is a list that will store integers, t is an integer in {1, 2, 3}, and v is an integer such that 1 <= v <= 10^9.
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
        
    #State: `start` is the maximum value of `v` when `t == 1`, `end` is the minimum value of `v` when `t == 2`, and `num` is a list of all `v` values when `t == 3`.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: `start` is the maximum value of `v` when `t == 1`, `end` is the minimum value of `v` when `t == 2`, and `num` is a list of all `v` values when `t == 3`; `count_num` is the number of elements in `num` that are within the range `[start, end]`.
    if (start > end) :
        return 0
        #The program returns 0
    #State: `start` is the maximum value of `v` when `t == 1`, `end` is the minimum value of `v` when `t == 2`, and `num` is a list of all `v` values when `t == 3`; `count_num` is the number of elements in `num` that are within the range `[start, end]`. Additionally, `start` is less than or equal to `end`.
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0
    #The program returns the value of `end - start + 1 - count_num` if `end - start + 1` is greater than or equal to `count_num`, otherwise it returns 0.
#Overall this is what the function does:The function reads a series of integer pairs, where each pair consists of a type `t` and a value `v`. It determines the maximum value `start` from pairs where `t` is 1, the minimum value `end` from pairs where `t` is 2, and collects all values `v` from pairs where `t` is 3 into a list `num`. It then counts how many values in `num` fall within the range `[start, end]`. Finally, it returns 0 if the range `[start, end]` is invalid (i.e., `start > end`) or if the number of values in `num` within the range exceeds the size of the range. Otherwise, it returns the difference between the size of the range and the count of values within the range.

