#State of the program right berfore the function call: n is a positive integer greater than or equal to 1.**
def func_1(n):
    x = ''.join([x.lower() for x in n if x.isalpha()])
    return x == x[::-1]
    #The program returns True if the string 'x' is a palindrome, meaning it reads the same forwards and backwards, and False otherwise.
#Overall this is what the function does:The function accepts a parameter `n`, which is a positive integer greater than or equal to 1. It then creates a new string `x` by converting `n` to lowercase letters and removing any non-alphabetic characters. Finally, the function returns True if the string `x` is a palindrome (reads the same forwards and backwards), and False otherwise.

