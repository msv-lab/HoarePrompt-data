#State of the program right berfore the function call: expression is a string that may contain characters such as parentheses, brackets, or braces that need to be checked for balance.
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: `stack` is empty if the brackets in `expression` are balanced; otherwise, it contains the unmatched opening brackets remaining. `expression` is a string that may contain parentheses, brackets, or braces, and if the loop does not execute, `stack` remains empty and `expression` has no characters.
    return not stack
    #The program returns True if the brackets in 'expression' are balanced (indicating 'stack' is empty) and returns False if there are unmatched opening brackets remaining in 'stack'.
#Overall this is what the function does:The function `func_1` checks whether the brackets (parentheses, curly braces, and square brackets) in the provided string `expression` are balanced. It maintains a stack to track opening brackets and ensures that for every closing bracket encountered, there is a corresponding and correctly ordered opening bracket. If the brackets are balanced, the function returns True; otherwise, it returns False. This includes cases with unmatched opening brackets, closed brackets without a matching opening bracket, or an empty input string, which is considered balanced. The function does not handle invalid characters explicitly and assumes input consists only of the specified bracket types or is empty.

