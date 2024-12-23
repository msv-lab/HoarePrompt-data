#State of the program right berfore the function call: snake_case_str is a string containing only lowercase letters and underscores.
def func_1(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = ''.join(word.capitalize() for word in words)
    return camel_case_str
    #The program returns camel_case_str which is formed by capitalizing each word in words (obtained by splitting snake_case_str at each underscore) and joining them without spaces
#Overall this is what the function does:This function accepts a parameter `snake_case_str`, which is a string containing only lowercase letters and underscores. It splits the string at each underscore to form a list of words, capitalizes each word in the list, and then joins them together without any spaces to form a new string `camel_case_str`. The function returns `camel_case_str`. The function handles the case where `snake_case_str` might be an empty string by returning an empty string. However, it does not handle the case where `snake_case_str` contains characters other than lowercase letters and underscores, which would result in unexpected behavior.

