#State of the program right berfore the function call: s is a string of length between 1 and 1000 consisting of only English letters.
def func_1(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
        
    #State of the program after the  for loop has been executed: The loop will return False if any character at index i and n - 1 - i in string s are not equal. Otherwise, it will return True.
    return True
    #The program returns True if all characters at index i and n - 1 - i in string s are equal, otherwise it returns False
#Overall this is what the function does:The function `func_1` accepts a string `s` of length between 1 and 1000 consisting of only English letters. It iterates through the string and checks if the characters at index i and n - 1 - i are equal. If all characters satisfy this condition, the function returns True; otherwise, it returns False.

