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
        
    #State of the program after the  for loop has been executed: `expression` is a string; `stack` is a list that contains only the opening brackets in the order they were encountered in `expression`. If `stack` is empty after the loop, `expression` contains balanced brackets. If `stack` is not empty, then `expression` contains unbalanced brackets.
    return not stack
    #The program returns True if the 'expression' contains balanced brackets (i.e., stack is empty), and returns False if the 'expression' contains unbalanced brackets (i.e., stack is not empty).
#Overall this is what the function does:The function accepts a string `expression` and checks for balanced brackets. It returns True if all opening brackets have corresponding closing brackets in the correct order, and returns False if the brackets are unbalanced or if a closing bracket appears without a matching opening bracket.

