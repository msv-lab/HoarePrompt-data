#State of the program right berfore the function call: n is a positive integer greater than 0.**
def func_1(n):
    x = ''.join([x.lower() for x in n if x.isalpha()])
    return x == x[::-1]
    #The program returns True if the positive integer 'n' is equal to its reverse, otherwise it returns False
#Overall this is what the function does:The function accepts a positive integer n, extracts the alphabetic characters, converts them to lowercase, and checks if the resulting string is equal to its reverse. It returns True if they are equal, otherwise it returns False. The function does not handle cases where n is not a string containing alphabetic characters, and it does not consider special characters or numeric values in the comparison.

