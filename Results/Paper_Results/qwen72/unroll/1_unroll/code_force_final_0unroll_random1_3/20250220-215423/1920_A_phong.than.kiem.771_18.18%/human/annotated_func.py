#State of the program right berfore the function call: isOne is a boolean value.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer value that is input by the user.
    else :
        return 1
        #The program returns 1.
#Overall this is what the function does:The function `func_1` accepts a boolean parameter `isOne`. If `isOne` is `False`, it prompts the user to input an integer and returns this integer value. If `isOne` is `True`, it returns the integer value 1. The function does not modify any external state or variables and only returns an integer based on the input parameter.

#State of the program right berfore the function call: space is a boolean indicating whether to split the input line by spaces, to_int is a boolean indicating whether to convert the split items to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: *`space` is a boolean indicating whether to split the input line by spaces, `to_int` is a boolean indicating whether to convert the split items to integers, `line` is an input string. If `space` is true, `items` is a list of strings obtained by splitting `line` by spaces. If `space` is false, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers obtained by converting each item in `items`. `items` is a list of strings derived from splitting the input string `line` by spaces, as `space` is true and `to_int` is also true.
    else :
        return items
        #The program returns a list of characters from the input string `line` if `space` is false. If `space` is true, it returns a list of strings obtained by splitting `line` by spaces. In both cases, the items are not converted to integers since `to_int` is false.
#Overall this is what the function does:The function `func_2` accepts two boolean parameters, `space` and `to_int`. It reads a line of input from the user. If `space` is true, it splits the input line by spaces into a list of strings. If `space` is false, it converts the input line into a list of characters. If `to_int` is true, it converts each item in the list to an integer and returns the list of integers. If `to_int` is false, it returns the list of strings or characters without conversion, depending on the value of `space`.

#State of the program right berfore the function call: arr is a list of integers, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: Output State: `string` is a string containing the elements of `arr` converted to strings, each followed by the string `sym`, concatenated together.
    return string
    #The program returns a string that contains the elements of `arr` converted to strings, each followed by the string `sym`, concatenated together.
#Overall this is what the function does:The function `func_3` takes a list of integers `arr` and a string `sym` as parameters. It returns a single string where each integer in `arr` is converted to a string, followed by the string `sym`, and all these parts are concatenated together. The final state of the program is that the function has returned this concatenated string, and the input parameters `arr` and `sym` remain unchanged.

