#State of the program right berfore the function call: isOne is a boolean value, where if it is False, the function reads and returns an integer input from the user, and if it is True, the function returns the integer 1.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer input from the user.
    else :
        return 1
        #The program returns 1
#Overall this is what the function does:The function accepts a boolean parameter `isOne`. If `isOne` is False, it returns an integer input from the user. If `isOne` is True, it returns the integer 1.

#State of the program right berfore the function call: space is a boolean indicating whether the input line should be split into items based on spaces, to_int is a boolean indicating whether the items should be converted to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: `space` is a boolean, `to_int` is a boolean, `line` is a string. If `space` is `True`, `items` is a list of substrings from `line` split by spaces. If `space` is `False`, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers where each element is the integer conversion of the corresponding element in `items`. If `space` is `True`, `items` consists of substrings split by spaces from `line`, and if `space` is `False`, `items` consists of individual characters from `line`. Each substring or character in `items` must be convertible to an integer for the conversion to succeed.
    else :
        return items
        #The program returns `items`, which is a list of substrings from `line` split by spaces if `space` is `True`, or a list of characters from `line` if `space` is `False`.
#Overall this is what the function does:The function reads a line of input and processes it based on the `space` and `to_int` parameters. If `space` is `True`, it splits the line into substrings separated by spaces; if `False`, it treats each character as a separate item. If `to_int` is `True`, it converts each item to an integer and returns the list of integers. If `to_int` is `False`, it returns the list of items (either substrings or characters) without conversion.

#State of the program right berfore the function call: arr is a list of values of any type, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: `arr` is a list of values of any type, `sym` is a string, `string` is a concatenated string of all elements in `arr` converted to strings, each followed by `sym`.
    return string
    #The program returns a concatenated string of all elements in `arr` converted to strings, each followed by `sym`.
#Overall this is what the function does:The function accepts a list of values (`arr`) and a string (`sym`). It returns a single string where each element from the list is converted to a string and concatenated with `sym` following each element.

