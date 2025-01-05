#State of the program right berfore the function call: n is a positive integer greater than or equal to 1.**
def func_1(n):
    x = ''.join([x.lower() for x in n if x.isalpha()])
    return x == x[::-1]
    #The program returns True if the value of x is equal to its reverse, otherwise it returns False.
#Overall this is what the function does:The function accepts a positive integer n and converts n into a string, keeping only the alphabetic characters in lowercase. It then checks if this modified string is equal to its reverse and returns True if they are equal, otherwise it returns False.

