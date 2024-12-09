#State of the program right berfore the function call: snake_str is a string consisting of lowercase letters and underscores, and it contains at least one underscore.
def func_1(snake_str):
    components = snake_str.split('_')
    return ''.join(x.capitalize() for x in components)
    #The program returns a string formed by joining the capitalized components of 'snake_str' after splitting it at each underscore.
#Overall this is what the function does:The function accepts a string `snake_str` containing lowercase letters and underscores, and returns a string formed by joining the capitalized segments of `snake_str` split by underscores, effectively converting it into camel case.

