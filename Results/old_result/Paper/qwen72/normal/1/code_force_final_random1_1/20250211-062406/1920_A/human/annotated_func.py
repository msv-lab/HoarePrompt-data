#State of the program right berfore the function call: isOne is a boolean value.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value entered by the user.
    else :
        return 1
        #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `True`, it returns the integer value 1. If `isOne` is `False`, it prompts the user to enter an integer and returns the entered integer value.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input line by spaces, to_int is a boolean indicating whether to convert the split items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *`space` is a boolean indicating whether to split the input line by spaces, `to_int` is a boolean indicating whether to convert the split items to integers, `line` is the input string provided by the user. If `space` is `True`, `items` is a list of strings obtained by splitting `line` by spaces. If `space` is `False`, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers converted from the items in `items`. If `space` is `True`, `items` contains strings obtained by splitting `line` by spaces. If `space` is `False`, `items` contains individual characters from `line`. Since `to_int` is `True`, each item in `items` is converted to an integer before being returned.
    else :
        return items
        #The program returns `items`, which is a list of characters from `line` if `space` is `False`. If `space` is `True`, `items` is a list of strings obtained by splitting `line` by spaces. Since `to_int` is `False`, no conversion to integers is performed.
#Overall this is what the function does:The function `func_2` takes two boolean parameters, `space` and `to_int`. It reads a line of input from the user. If `space` is `True`, the line is split into a list of strings based on spaces. If `space` is `False`, the line is treated as a sequence of characters, resulting in a list of characters. If `to_int` is `True`, each item in the list is converted to an integer. The function returns a list of integers if `to_int` is `True`, or a list of strings/characters if `to_int` is `False`.

#State of the program right berfore the function call: arr is a list of elements that can be converted to strings, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: `arr` is a list of elements that can be converted to strings, `sym` is a string, `string` is now equal to the concatenation of each element in `arr` converted to a string followed by `sym`, except for the last element which is not followed by `sym`.
    return string
    #The program returns a string that is the concatenation of each element in `arr` converted to a string, followed by `sym`, except for the last element which is not followed by `sym`.
#Overall this is what the function does:The function `func_3` takes two parameters: `arr`, a list of elements that can be converted to strings, and `sym`, a string. It returns a single string that is the result of concatenating each element in `arr` (converted to a string) followed by `sym`, except that `sym` is not appended after the last element in `arr`. After the function concludes, the input parameters `arr` and `sym` remain unchanged, and the returned string reflects the described concatenation.

#State of the program right berfore the function call: string is a string, and substring is a non-empty string.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: `string` is a string that contains `substring`. `substring` is a non-empty string. `indices` is a list containing all the indices of every occurrence of `substring` in `string`. `index` is `-1`, indicating that there are no more occurrences of `substring` in `string` after the last found index.
    return indices
    #The program returns a list `indices` containing all the indices of every occurrence of `substring` in `string`.
#Overall this is what the function does:The function `func_4` accepts two parameters: `string` (a string) and `substring` (a non-empty string). It returns a list of integers representing the starting indices of every occurrence of `substring` within `string`. If `substring` does not occur in `string`, the function returns an empty list. After the function concludes, the input parameters remain unchanged, and the returned list contains all the indices where `substring` starts in `string`.

#State of the program right berfore the function call: arr is a list of integers, and element is an integer.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices where the value in the list `arr` matches the integer `element`. Each index in the returned list corresponds to a position in `arr` where the value is equal to `element`.
#Overall this is what the function does:The function `func_5` accepts a list of integers `arr` and an integer `element`. It returns a list of indices where the value in `arr` matches `element`. Each index in the returned list corresponds to a position in `arr` where the value is equal to `element`. If no matches are found, an empty list is returned.

#State of the program right berfore the function call: arr is a list of lists where each sublist contains at least `index + 1` elements, index is a non-negative integer, and value is an integer.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: `arr` is a list of lists where each sublist contains at least `index + 1` elements, `index` is a non-negative integer, `value` is an integer, and the loop has iterated through all sublists in `arr`. For each sublist `subArray` in `arr`, the element at position `index` in `subArray` is not equal to `value`. The loop did not return any sublist because no sublist in `arr` had an element at position `index` that was equal to `value`.
    return None
    #The program returns None, indicating that no sublist in `arr` had an element at position `index` that was equal to `value`.
#Overall this is what the function does:The function `func_6` takes a list of lists `arr`, a non-negative integer `index`, and an integer `value`. It searches through each sublist in `arr` to find the first sublist where the element at position `index` is equal to `value`. If such a sublist is found, it is returned. If no sublist meets this condition, the function returns `None`. After the function concludes, `arr`, `index`, and `value` remain unchanged, and the function either returns a matching sublist or `None`.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100. start and end are floating-point numbers initialized to -1 and 1000000000.0 respectively. num is an empty list.
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
        
    #State: After all iterations, `n` is the total number of iterations performed, `i` is `n-1`, `start` is the maximum value encountered when `t` is 1, `end` is the minimum value encountered when `t` is 2, and `num` is a list containing all values encountered when `t` is 3. The initial values of `start` and `end` remain unchanged if no updates were made during the loop.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: After all iterations, `n` is the total number of elements in `num`, `i` is the last element in `num`, `start` remains the maximum value encountered when `t` is 1, `end` remains the minimum value encountered when `t` is 2, `num` contains all values encountered when `t` is 3, and `count_num` is the number of elements in `num` that are between `start` and `end` (inclusive).
    if (start > end) :
        return 0
        #The program returns 0.
    #State: After all iterations, `n` is the total number of elements in `num`, `i` is the last element in `num`, `start` remains the maximum value encountered when `t` is 1, `end` remains the minimum value encountered when `t` is 2, `num` contains all values encountered when `t` is 3, `count_num` is the number of elements in `num` that are between `start` and `end` (inclusive), and `start` is less than or equal to `end`.
    return end - start + 1 - count_num if end - start + 1 >= count_num else 0
    #The program returns the difference between `end` and `start` plus 1 minus `count_num` if `end - start + 1` is greater than or equal to `count_num`; otherwise, it returns 0. Here, `start` is the maximum value encountered when `t` is 1, `end` is the minimum value encountered when `t` is 2, and `count_num` is the number of elements in `num` that are between `start` and `end` (inclusive).
#Overall this is what the function does:The function `func_7` reads an integer `n` from the user, indicating the number of operations to perform. It then processes `n` lines of input, each containing two integers `t` and `v`. Based on the value of `t`, the function updates the `start` and `end` values or appends `v` to the list `num`. After processing all inputs, the function calculates the number of elements in `num` that fall within the range `[start, end]` (inclusive). If `start` is greater than `end`, the function returns 0. Otherwise, it returns the difference between `end` and `start` plus 1, minus the count of elements in `num` that fall within the range, ensuring the result is non-negative.

