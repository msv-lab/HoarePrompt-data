#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10100000.**
def func_1(n):
    x = ''.join([x.lower() for x in n if x.isalpha()])
    return x == x[::-1]
    #The program returns True if the positive integer 'n' is a palindrome (reads the same forwards and backwards), otherwise it returns False.
#Overall this is what the function does:The function func_1 accepts a positive integer n and converts it to a string, keeping only the alphabetical characters in lowercase. It then checks if the resulting string is a palindrome (reads the same forwards and backwards) and returns True if it is, otherwise it returns False. Note that if n contains no alphabetical characters, the function will always return True since an empty string is considered a palindrome.

