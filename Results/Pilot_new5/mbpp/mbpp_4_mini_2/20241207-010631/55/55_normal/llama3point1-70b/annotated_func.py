#State of the program right berfore the function call: snake_case_str is a string consisting of lowercase letters, underscores, and possibly empty, where underscores separate words.
def func_1(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = ''.join(word.capitalize() for word in words)
    return camel_case_str
    #The program returns the camelCase string formed by joining the capitalized words from the list of substrings obtained by splitting the snake_case string at underscores.
#Overall this is what the function does:The function accepts a string `snake_case_str` consisting of lowercase letters and underscores. It returns a camelCase string formed by capitalizing each word separated by underscores in the input string. The function will also correctly handle an empty string by returning an empty string. If the input string does not contain underscores, it capitalizes the entire string as a single word.

