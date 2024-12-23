def func_1(snake_case_str):
    words = snake_case_str.split('_')
    camel_case_str = ''.join((word.capitalize() for word in words))
    return camel_case_str