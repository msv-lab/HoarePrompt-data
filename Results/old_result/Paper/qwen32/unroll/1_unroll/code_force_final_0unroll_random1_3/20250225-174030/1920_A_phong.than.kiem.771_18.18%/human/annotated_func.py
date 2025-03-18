#State of the program right berfore the function call: isOne is a boolean value. If isOne is False, the function reads and returns an integer from the input. If isOne is True, the function returns the integer 1.
def func_1(isOne):
    if (not isOne) :
        return int(input())
        #The program returns an integer that is read from the input.
    else :
        return 1
        #The program returns the integer 1.
#Overall this is what the function does:The function accepts a boolean parameter `isOne`. If `isOne` is `False`, it reads and returns an integer from the input. If `isOne` is `True`, it returns the integer 1.

#State of the program right berfore the function call: space is a boolean indicating whether the input line should be split into multiple items, and to_int is a boolean indicating whether the items should be converted to integers.
def func_2(space, to_int):
    line = input()
    if space :
        items = line.split()
    else :
        items = list(line)
    #State: `space` is a boolean, `to_int` is a boolean, `line` is the input string provided by the user. If `space` is True, `items` is a list of substrings from `line` split by whitespace. Otherwise, `items` is a list of characters from `line`.
    if to_int :
        return [int(i) for i in items]
        #The program returns a list of integers, where each integer is derived from converting each substring in `items` to an integer. If `space` is True, `items` is a list of substrings from `line` split by whitespace. Otherwise, `items` is a list of characters from `line`. Since `to_int` is True, each element in `items` is converted to an integer.
    else :
        return items
        #The program returns `items`, which is a list of characters from `line` since `space` is False.
#Overall this is what the function does:The function takes two boolean parameters, `space` and `to_int`. It reads a line of input from the user. If `space` is True, it splits the line into substrings based on whitespace; otherwise, it splits the line into individual characters. If `to_int` is True, it converts each substring or character into an integer. The function returns a list of these integers or characters, depending on the `to_int` parameter.

#State of the program right berfore the function call: arr is a list of elements, and sym is a string that will be used as a separator between the elements of arr when they are concatenated into a single string.
def func_3(arr, sym):
    string = ''
    for i in arr:
        string += str(i) + sym
        
    #State: `arr` is a list of elements, `sym` is a string, `string` is a concatenated string of all elements in `arr` with `sym` inserted between each element.
    return string
    #The program returns a concatenated string of all elements in `arr` with `sym` inserted between each element.
#Overall this is what the function does:The function takes a list of elements (`arr`) and a string (`sym`) as input, and returns a single string where all elements of `arr` are concatenated with `sym` inserted between each element.

