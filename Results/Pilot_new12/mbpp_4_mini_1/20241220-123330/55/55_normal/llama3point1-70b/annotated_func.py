#State of the program right berfore the function call: snake_case_str is a string consisting of lowercase letters and underscores, where words are separated by underscores.
def func_1(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = ''.join(word.capitalize() for word in words)
    return camel_case_str
    #The program returns the string in camel case format created from the original snake_case string `snake_case_str`
#Overall this is what the function does:The function accepts a single parameter `snake_case_str`, which is expected to be a string comprising lowercase letters and underscores. It splits this string into individual words using underscores as delimiters, capitalizes the first letter of each word, and then concatenates these words into a single camel case string (with no underscores). The function returns this camel case string. However, it does not handle cases where `snake_case_str` is empty or contains leading, trailing, or consecutive underscores, which could lead to unexpected results in terms of the output format.

