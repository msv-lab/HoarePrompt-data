#State of the program right berfore the function call: snake_case_str is a string containing only lowercase letters and underscores.
def func_1(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = ''.join(word.capitalize() for word in words)
    return camel_case_str
    #`camel_case_str` is the transformed version of `snake_case_str` where each word is capitalized and joined without any separators; `words` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a single parameter `snake_case_str`, which is a string containing only lowercase letters and underscores. It splits the string into individual words based on the underscores, capitalizes the first letter of each word, and joins them together without any separators to form a `camelCase` string. The function then returns this `camelCase` string. The internal list `words` remains unchanged throughout the process. The function handles the case where `snake_case_str` is an empty string by returning an empty string.

