#State of the program right berfore the function call: expression is a string containing parentheses, brackets, and/or braces.
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: `stack` is empty if all brackets in `expression` are matched; otherwise, `stack` contains unmatched opening brackets. `expression` is processed completely.
    return not stack
    #The program returns True if all brackets in 'expression' are matched, and False if there are unmatched opening brackets in 'stack'.
#Overall this is what the function does:The function `func_1` accepts a string `expression` that contains parentheses, brackets, and braces. It checks whether all the opening brackets in the expression have matching closing brackets in the correct order. The function uses a stack data structure to keep track of the unmatched opening brackets. If it encounters a closing bracket without a corresponding unmatched opening bracket on the stack, it returns `False`. Additionally, if there are any unmatched opening brackets remaining in the stack after processing the entire expression, it also returns `False`. Conversely, if all brackets are matched correctly, it returns `True`. The function does not account for characters in the expression that are not brackets, meaning they are effectively ignored.

