#State of the program right berfore the function call: isOne is a boolean value. If isOne is False, the function reads and returns an integer from the input. If isOne is True, the function returns the integer 1.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer that is read from the input.
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
    #State: `space` is a boolean, `to_int` is a boolean, `line` is a string. If `space` is True, `items` is a list of substrings obtained by splitting `line` based on spaces. If `space` is False, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers where each integer is obtained by converting each element in the list `items` to an integer. If `space` is True, `items` is a list of substrings split from `line` by spaces, and if `space` is False, `items` is a list of characters from `line`. Since `to_int` is True, each element in `items` is converted to an integer.
    else :
        return items
        #The program returns `items`, which is a list of substrings obtained by splitting `line` based on spaces if `space` is True, or a list of characters from `line` if `space` is False. Since `to_int` is False, the items are not converted to integers.
#Overall this is what the function does:The function reads a line of input and processes it based on two boolean parameters. If `space` is True, it splits the line into substrings separated by spaces; if `space` is False, it splits the line into individual characters. If `to_int` is True, it converts each element in the resulting list to an integer. The function returns a list of integers if `to_int` is True, or a list of strings (substrings or characters) if `to_int` is False.

#State of the program right berfore the function call: arr is a list of elements, and sym is a string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: `arr` is a list of elements, `sym` is a string, `string` is a string that concatenates all elements of `arr` with `sym` appended after each element except the last one.
    return string
    #The program returns the string that concatenates all elements of `arr` with `sym` appended after each element except the last one.
#Overall this is what the function does:The function takes a list of elements and a string, and returns a single string that concatenates all elements of the list with the given string appended after each element except the last one.

