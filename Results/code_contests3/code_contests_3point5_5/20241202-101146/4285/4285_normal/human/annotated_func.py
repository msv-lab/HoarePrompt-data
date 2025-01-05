#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10100000.**
def func_1(n):
    x = ''.join([x.lower() for x in n if x.isalpha()])
    return x == x[::-1]
    #The program returns an AttributeError
#Overall this is what the function does:The function accepts a positive integer n within the range 1 <= n <= 10100000. It then tries to convert n to lowercase and filter out non-alphabetic characters, resulting in an AttributeError due to attempting string manipulation on an integer input.

