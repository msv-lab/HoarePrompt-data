#State of the program right berfore the function call: n is a positive integer greater than or equal to 1.**
def func_1(n):
    x = ''.join([x.lower() for x in n if x.isalpha()])
    return x == x[::-1]
    #The program returns True if the string x is a palindrome (reads the same forwards and backwards), otherwise it returns False
#Overall this is what the function does:The function accepts a positive integer n, extracts the alphabetic characters from n, converts them to lowercase, and checks if the resulting string is a palindrome. It returns True if the string is a palindrome, otherwise it returns False. Edge cases or missing logic to consider: The function does not handle cases where n is not a string or if there are no alphabetic characters in n.

