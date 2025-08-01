#State of the program right berfore the function call: isOne is a boolean value.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value entered by the user.
    else :
        return 1
        #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `False`, it prompts the user to enter an integer and returns that integer. If `isOne` is `True`, it returns the integer 1. The function modifies the program state by returning either the user-input integer or the integer 1, depending on the value of `isOne`.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input by spaces, to_int is a boolean indicating whether to convert the items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *space is a boolean indicating whether to split the input by spaces, to_int is a boolean indicating whether to convert the items to integers, and line is the user input. If space is True, items is a list of strings obtained by splitting `line` by spaces. If space is False, items is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers converted from the items in `items`. If `space` is True, `items` is a list of strings obtained by splitting the user input `line` by spaces. If `space` is False, `items` is a list of individual characters from the user input `line`. Since `to_int` is True, each item in `items` is converted to an integer before being returned.
    else :
        return items
        #The program returns a list of characters from `line` if `space` is False, or a list of strings obtained by splitting `line` by spaces if `space` is True. Since `to_int` is False, the items are not converted to integers.
#Overall this is what the function does:The function `func_2` takes two boolean parameters, `space` and `to_int`. It reads a line of input from the user. If `space` is True, it splits the input by spaces; otherwise, it splits the input into individual characters. If `to_int` is True, it converts each item in the resulting list to an integer. The function returns a list of integers if `to_int` is True, or a list of strings/characters if `to_int` is False. The final state of the program is that the function has returned one of these lists based on the input parameters.

#State of the program right berfore the function call: arr is a list of elements that can be converted to strings, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: `arr` is a list of elements that can be converted to strings, `sym` is a string, `string` is now equal to the concatenation of the string representations of all elements in `arr`, each followed by `sym`, except for the last element which is not followed by `sym`.
    return string
    #The program returns a string that is the concatenation of the string representations of all elements in `arr`, each followed by `sym`, except for the last element which is not followed by `sym`.
#Overall this is what the function does:The function `func_3` takes two parameters: `arr`, a list of elements that can be converted to strings, and `sym`, a string. It returns a single string that is the concatenation of the string representations of all elements in `arr`, with each element followed by `sym`, except for the last element which is not followed by `sym`. The original `arr` and `sym` remain unchanged.

#State of the program right berfore the function call: string is a string, and substring is a non-empty string.
def func_4(string, substring):
    indices = []
    index = string.find(substring)
    while index != -1:
        indices.append(index)
        
        index = string.find(substring, index + 1)
        
    #State: string is a string, substring is a non-empty string, indices is a list containing all the starting positions of substring in string, index is -1.
    return indices
    #The program returns a list containing all the starting positions of the substring in the string.
#Overall this is what the function does:The function `func_4` takes two parameters: `string` (a string) and `substring` (a non-empty string). It returns a list of integers representing the starting positions of all occurrences of `substring` within `string`. If `substring` is not found in `string`, the function returns an empty list. After the function concludes, the original `string` and `substring` remain unchanged, and the returned list contains the indices of the starting positions of `substring` in `string`.

#State of the program right berfore the function call: arr is a list of integers, and element is an integer.
def func_5(arr, element):
    return [index for index, value in enumerate(arr) if value == element]
    #The program returns a list of indices where the value in the list `arr` matches the integer `element`. Each index in the returned list corresponds to a position in `arr` where the element at that position is equal to `element`.
#Overall this is what the function does:The function `func_5` takes two parameters: `arr`, a list of integers, and `element`, an integer. It returns a list of indices where the elements in `arr` are equal to `element`. If no elements in `arr` match `element`, the function returns an empty list. The original list `arr` remains unchanged.

#State of the program right berfore the function call: arr is a list of lists where each sublist contains at least `index + 1` elements, index is a non-negative integer, and value is an integer.
def func_6(arr, index, value):
    for subArray in arr:
        if subArray[index] == value:
            return subArray
        
    #State: `arr` is a list of lists where each sublist contains at least `index + 1` elements, `index` is a non-negative integer, `value` is an integer, and the loop has iterated through all sublists in `arr`. If any sublist in `arr` has an element at position `index` equal to `value`, the program returns that sublist. If no sublist in `arr` has an element at position `index` equal to `value`, the program does not return anything.
    return None
    #The program returns None, indicating that no sublist in `arr` had an element at position `index` equal to `value`.
#Overall this is what the function does:The function `func_6` takes three parameters: `arr` (a list of lists), `index` (a non-negative integer), and `value` (an integer). It searches through `arr` to find the first sublist where the element at the specified `index` matches `value`. If such a sublist is found, it is returned. If no sublist meets this condition, the function returns `None`. The function does not modify the input parameters.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 100. start and end are initialized as -1 and 1000000000 respectively. num is an empty list.
def func_7():
    n = int(input())
    start = -1
    end = int(1000000000.0)
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
        
    #State: After the loop executes all `n` iterations, `i` is `n-1`, `num` is a list containing all the integers `v` for which `t` was 3 during the iterations. `start` is the maximum value of `v` encountered when `t` was 1, or remains -1 if no such `v` was greater than the initial `start`. `end` is the minimum value of `v` encountered when `t` was 2, or remains 1000000000 if no such `v` was less than the initial `end`. The value of `n` remains unchanged.
    count_num = 0
    for i in num:
        if i < start or i > end:
            continue
        else:
            count_num += 1
        
    #State: After the loop executes all the iterations, `num` contains all the integers as it did initially, `i` is the last integer in `num`, `start` and `end` remain unchanged, and `count_num` is the total number of integers in `num` that fall within the range `[start, end]`.
    return end - start + 1 - count_num if start <= end else 0
    #The program returns the difference between `end` and `start` plus 1 minus `count_num` if `start` is less than or equal to `end`; otherwise, it returns 0. Here, `end` and `start` are the same as they were initially, and `count_num` is the total number of integers in `num` that fall within the range `[start, end]`.
#Overall this is what the function does:The function `func_7` processes a series of inputs to determine a specific count and range. It starts by reading an integer `n` (where 2 ≤ n ≤ 100), followed by `n` pairs of integers `(t, v)`. Based on the value of `t`, it updates the values of `start` and `end` and collects certain values of `v` into a list `num`. After processing all inputs, it calculates the number of elements in `num` that fall within the range `[start, end]`. Finally, it returns the difference between `end` and `start` plus 1, minus this count, if `start` is less than or equal to `end`; otherwise, it returns 0. The function modifies the values of `start`, `end`, and `num` internally but does not affect any external variables.

