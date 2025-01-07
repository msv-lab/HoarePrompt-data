#State of the program right berfore the function call: snake_case_str is a string that consists of lowercase letters and underscores, where words are separated by underscores.
def func_1(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = ''.join(word.capitalize() for word in words)
    return camel_case_str
    #The program returns the string 'camel_case_str', which is the concatenation of the capitalized words obtained from splitting 'snake_case_str' by underscores.
#Overall this is what the function does:The function accepts a string `snake_case_str` consisting of lowercase letters and underscores, and returns its camel case equivalent by concatenating the capitalized words obtained from splitting `snake_case_str` by underscores. No checks are made for empty strings or strings that do not contain underscores, which would affect the output. If `snake_case_str` is empty, the function will return an empty string.

