#State of the program right berfore the function call: isOne is a boolean value.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value entered by the user.
    else :
        return 1
        #The program returns the integer 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `False`, it prompts the user to enter an integer and returns that integer. If `isOne` is `True`, it returns the integer 1.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input by spaces, to_int is a boolean indicating whether to convert the split items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *`space` is a boolean indicating whether to split the input by spaces, `to_int` is a boolean indicating whether to convert the split items to integers, `line` is the input string. If `space` is true, `items` is a list of strings split from `line` by spaces. If `space` is false, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers converted from the items in `items`. If `space` is true, `items` contains strings split from `line` by spaces. If `space` is false, `items` contains individual characters from `line`. Since `to_int` is true, each item in `items` is converted to an integer before being returned.
    else :
        return items
        #The program returns a list of characters from the input string `line`.
#Overall this is what the function does:The function `func_2` accepts two boolean parameters, `space` and `to_int`. It reads a line of input from the user. If `space` is `True`, it splits the input line into a list of strings based on spaces. If `space` is `False`, it splits the input line into a list of individual characters. If `to_int` is `True`, it converts each item in the list to an integer and returns the list of integers. If `to_int` is `False`, it returns the list of strings or characters without conversion.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string used as a separator.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: Output State: `string` is a string containing the elements of `arr` converted to strings, each followed by the `sym` separator, concatenated together. The final `sym` separator will be at the end of the string. The list `arr` and the string `sym` remain unchanged.
    return string
    #The program returns a string that contains the elements of `arr` converted to strings, each followed by the `sym` separator, concatenated together, with the final `sym` separator at the end of the string. The list `arr` and the string `sym` remain unchanged.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a string `sym`. It returns a string where each element of `arr` is converted to a string, followed by `sym`, and the final `sym` is included at the end of the string. The list `arr` and the string `sym` remain unchanged.

