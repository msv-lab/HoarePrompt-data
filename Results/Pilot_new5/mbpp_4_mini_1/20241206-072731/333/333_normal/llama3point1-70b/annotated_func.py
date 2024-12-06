#State of the program right berfore the function call: expression is a string that may contain various characters including parentheses, brackets, and braces.
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: `expression` is a string that may contain any characters, `stack` is an empty list if all brackets are matched and closed properly or contains unmatched opening brackets if there are any, the length of `stack` represents the number of unmatched opening brackets. The function returns True if all brackets are matched and False if there is any unmatched opening bracket.
    return not stack
    #The program returns True if all brackets in 'expression' are matched and closed properly, and False if there are unmatched opening brackets in 'stack'.
#Overall this is what the function does:The function accepts a string `expression` and checks for balanced parentheses, brackets, and braces. It returns True if all opening brackets are correctly matched and closed by their corresponding closing brackets; otherwise, it returns False. The function does not account for other characters in the string, which may lead to misinterpretation of balanced expressions if they are present alongside brackets.

