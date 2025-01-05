#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^100000.
def func_1(n):
    x = ''.join([x.lower() for x in n if x.isalpha()])
    return x == x[::-1]
    #The program returns True because an empty string is equal to its reverse
#Overall this is what the function does:The function accepts a string `n`, filters it to retain only alphabetic characters converted to lowercase, and returns True if the resulting string is a palindrome or empty; otherwise, it returns False.

