#State of the program right berfore the function call: isOne is a boolean value indicating whether to return an integer input or always return 1. If isOne is False, the function returns an integer input; if isOne is True, the function always returns 1.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns 1
    else :
        return 1
        #The program returns 1 regardless of the value of isOne.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `False`, it reads an integer input from the user and returns it. If `isOne` is `True`, it disregards any input and always returns the integer `1`. In both cases, the final state of the program is that it has returned either the user's input or the integer `1`.

#State of the program right berfore the function call: t is an integer representing the number of test cases, and each test case consists of n constraints where n is an integer. Each constraint is represented by two integers a and x, where a is either 1, 2, or 3, and x is an integer between 1 and 10^9. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: `t` is an integer representing the number of test cases, and each test case consists of n constraints where n is an integer. Each constraint is represented by two integers a and x, where a is either 1, 2, or 3, and x is an integer between 1 and 10^9. There is at least one constraint of type 1 and one constraint of type 2, and no two constraints are the same. If `space` is True, `line` is split into a list of strings stored in `items`. Otherwise, `items` is a list of characters from a line.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers converted from the items in the list `items` where `to_int` is True and `space` is True, meaning `line` is split into a list of strings stored in `items`.
    else :
        return items
        #The program returns the list `items` which contains characters from a line without being split into a list of strings.
#Overall this is what the function does:The function `func_2` accepts two parameters: `space` (a boolean) and `to_int` (a boolean). Based on these parameters, it processes an input line (`line`). If both `to_int` and `space` are `True`, it splits the line into a list of strings, converts those strings to integers, and returns the resulting list of integers. If `to_int` is `False` or `space` is `False`, it simply returns the list of characters from the line as is, without any conversion or splitting.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string representing a separator (e.g., ' ', ',', etc.).
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: Output State: `string` is a concatenation of all integers in `arr` separated by `sym`.
    return string
    #The program returns a string that is the concatenation of all integers in the list `arr`, separated by `sym`
#Overall this is what the function does:The function accepts a list of integers `arr` and a string `sym`. It concatenates all integers in the list `arr`, using `sym` as the separator, and returns the resulting string.

