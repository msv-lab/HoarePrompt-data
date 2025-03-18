#State of the program right berfore the function call: isOne is a boolean value.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value provided by the user input.
    else :
        return 1
        #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `True`, it returns the integer value 1. If `isOne` is `False`, it returns an integer value provided by the user input.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input line by spaces, and to_int is a boolean indicating whether to convert the split items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *`space` is a boolean indicating whether to split the input line by spaces, `to_int` is a boolean indicating whether to convert the split items to integers, `line` is the input string. If `space` is true, `items` is a list of substrings split from `line` by spaces. If `space` is false, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers converted from the substrings in `items`. `items` is a list of substrings split from the input string `line` by spaces, as `space` is true and `to_int` is true.
    else :
        return items
        #The program returns a list of characters from the input string `line`, since `space` is false and `to_int` is false.
#Overall this is what the function does:The function `func_2` accepts two boolean parameters, `space` and `to_int`. It reads a line of input from the user. If `space` is true, it splits the input line into a list of substrings based on spaces. If `space` is false, it converts the input line into a list of individual characters. If `to_int` is true, it converts each item in the list to an integer and returns the list of integers. If `to_int` is false, it returns the list of substrings or characters as is.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: Output State: `string` is a string containing the elements of `arr` converted to strings, each followed by `sym`, concatenated together.
    return string
    #The program returns a string that contains the elements of `arr` converted to strings, each followed by `sym`, concatenated together.
#Overall this is what the function does:The function `func_3` accepts a list of integers `arr` and a string `sym`. It returns a string where each integer from `arr` is converted to a string, followed by `sym`, and all these are concatenated together. The final state of the program after the function concludes is that the returned string contains the elements of `arr` as strings, each followed by `sym`, in the order they appear in `arr`.

