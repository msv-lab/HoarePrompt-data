#State of the program right berfore the function call: isOne is a boolean value.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value that is input by the user.
    else :
        return 1
        #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `True`, it returns the integer value 1. If `isOne` is `False`, it prompts the user to input an integer and returns that integer. In both cases, the function returns an integer value.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input line by spaces, to_int is a boolean indicating whether to convert the items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *`space` is a boolean indicating whether to split the input line by spaces, `to_int` is a boolean indicating whether to convert the items to integers, `line` is the input string provided by the user. If `space` is `True`, `items` is a list of strings obtained by splitting `line` by spaces. If `space` is `False`, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers, where each integer is the result of converting the corresponding item in `items` to an integer. The `items` list is derived from the `line` input string: if `space` is `True`, `items` contains substrings obtained by splitting `line` by spaces; if `space` is `False`, `items` contains individual characters from `line`. Since `to_int` is `True`, each item in `items` is converted to an integer before being returned in the list.
    else :
        return items
        #The program returns `items`, which is a list of characters from `line` if `space` is `False`. If `space` is `True`, `items` is a list of strings obtained by splitting `line` by spaces. Since `to_int` is `False`, no conversion to integers is performed.
#Overall this is what the function does:The function `func_2` takes two boolean parameters, `space` and `to_int`. It reads a line of input from the user. If `space` is `True`, it splits the input line by spaces into a list of substrings. If `space` is `False`, it splits the input line into a list of individual characters. If `to_int` is `True`, it converts each element in the list to an integer and returns the list of integers. If `to_int` is `False`, it returns the list of substrings or characters without any conversion.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: `arr` is a list of integers that must have at least as many elements as it initially had, `i` is the last element of `arr`, `sym` is a string, `string` is now equal to the concatenation of the string representations of each element in `arr` followed by `sym`, except for the last element which is not followed by `sym`.
    return string
    #The program returns a string that is the concatenation of the string representations of each element in `arr`, followed by `sym`, except for the last element which is not followed by `sym`.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a string `sym`. It returns a string where each integer in `arr` is converted to its string representation and concatenated together, with `sym` inserted between each element, except after the last element. The original list `arr` remains unchanged.

#State of the program right berfore the function call: string is a string, and substring is a string that may or may not be present in string.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: `string` is a string, `substring` is a string that is present in `string`, `indices` is a list containing all the indices of the occurrences of `substring` in `string`, `index` is `-1`.
    return indices
    #The program returns a list containing all the indices of the occurrences of `substring` in `string`.
#Overall this is what the function does:The function `func_4` accepts two parameters, `string` and `substring`, both of which are strings. It returns a list of integers representing the starting indices of all occurrences of `substring` within `string`. If `substring` is not found in `string`, the function returns an empty list.

#State of the program right berfore the function call: arr is a list of integers, and element is an integer.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices where each index corresponds to the position in the list `arr` where the value equals `element`.
#Overall this is what the function does:The function `func_5` accepts a list of integers `arr` and an integer `element`. It returns a list of indices where each index corresponds to the position in `arr` where the value equals `element`. If no such elements exist, it returns an empty list.

#State of the program right berfore the function call: arr is a list of lists, index is a non-negative integer, and value is an integer.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: `arr` is a list of lists, `index` is a non-negative integer, and `value` is an integer. The loop has iterated through all sublists in `arr`. If any sublist `subArray` in `arr` has an element at position `index` that equals `value`, the function returns that `subArray`. If no such sublist is found, the function does not return anything.
    return None
    #The program returns None, indicating that no sublist in `arr` had an element at position `index` that equals `value`.
#Overall this is what the function does:The function `func_6` accepts a list of lists `arr`, a non-negative integer `index`, and an integer `value`. It searches through each sublist in `arr` to find the first one where the element at the specified `index` equals `value`. If such a sublist is found, it is returned. If no sublist meets this criterion, the function returns `None`. The function does not modify the input parameters.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100. start and end are floating-point numbers initialized to -1 and 1000000000.0 respectively. num is an initially empty list.
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
        
    #State: After all iterations of the loop, `n` is the number of iterations completed, `i` is `n-1`, `start` is the maximum value encountered when `t` was 1, `end` is the minimum value encountered when `t` was 2, and `num` is a list containing all values of `v` encountered when `t` was 3. The initial values of `start` (-1) and `end` (1000000000.0) are updated only if conditions within the loop are met.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: After all iterations of the loop, `n` is the total number of elements in `num`, `i` is the last element in `num`, `start` remains the maximum value encountered when `t` was 1, `end` remains the minimum value encountered when `t` was 2, `num` contains all values of `v` encountered when `t` was 3, and `count_num` is the count of elements in `num` that are within the range `[start, end]` (inclusive).
    if (start > end) :
        return 0
        #The program returns 0.
    #State: After all iterations of the loop, `n` is the total number of elements in `num`, `i` is the last element in `num`, `start` remains the maximum value encountered when `t` was 1, `end` remains the minimum value encountered when `t` was 2, `num` contains all values of `v` encountered when `t` was 3, and `count_num` is the count of elements in `num` that are within the range `[start, end]` (inclusive). Additionally, `start` is less than or equal to `end`.
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0
    #The program returns the difference between `end` and `start` plus 1 minus `count_num` if `end - start + 1` is greater than or equal to `count_num`; otherwise, it returns 0. Here, `end` is the minimum value encountered when `t` was 2, `start` is the maximum value encountered when `t` was 1, and `count_num` is the count of elements in `num` that are within the range `[start, end]` (inclusive).
#Overall this is what the function does:The function `func_7` reads an integer `n` and processes `n` pairs of integers `(t, v)` from the user. It updates two boundary values, `start` and `end`, based on the type `t` of each pair. If `t` is 1, `start` is updated to the maximum of its current value and `v`. If `t` is 2, `end` is updated to the minimum of its current value and `v`. If `t` is 3, `v` is added to a list `num`. After processing all pairs, the function counts the number of elements in `num` that fall within the range `[start, end]` (inclusive), denoted as `count_num`. If `start` is greater than `end`, the function returns 0. Otherwise, it returns the difference between `end` and `start` plus 1 minus `count_num`, unless this difference is less than `count_num`, in which case it also returns 0.

