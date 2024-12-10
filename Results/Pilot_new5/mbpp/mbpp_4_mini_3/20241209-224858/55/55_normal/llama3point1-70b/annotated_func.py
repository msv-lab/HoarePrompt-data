#State of the program right berfore the function call: snake_case_str is a string that consists of lowercase letters, underscores, and may contain multiple words separated by underscores.
def func_1(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = ''.join(word.capitalize() for word in words)
    return camel_case_str
    #The program returns the string `camel_case_str`, which is formed by joining the capitalized words in the list `words` obtained from splitting `snake_case_str` by underscores.
#Overall this is what the function does:The function accepts a string `snake_case_str` that consists of lowercase letters and underscores. It splits this string into words using underscores as delimiters, capitalizes the first letter of each word, and then joins these capitalized words together into a single string without any underscores. It returns this new string in camel case format. If `snake_case_str` is empty, the function will return an empty string.

