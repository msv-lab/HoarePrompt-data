#State of the program right berfore the function call: snake_case_str is a string that contains only lowercase letters, numbers, and underscores, and does not start or end with an underscore.
def func_1(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = ''.join(word.capitalize() for word in words)
    return camel_case_str
    #The program returns camel_case_str, which is the result of concatenating the capitalized elements of the list 'words' derived from the snake_case_str string containing only lowercase letters, numbers, and underscores.
#Overall this is what the function does:The function accepts a string `snake_case_str` that contains only lowercase letters, numbers, and underscores, and converts it to camel case format by capitalizing the first letter of each word separated by underscores and concatenating them. If `snake_case_str` is an empty string, the function returns an empty string as well.

