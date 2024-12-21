#State of the program right berfore the function call: expression is a string containing only parentheses ('(', ')'), curly braces ('{', '}'), and square brackets ('[', ']').
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: `expression` is a non-empty string containing only parentheses, curly braces, and square brackets, `stack` is an empty list if and only if every opening bracket has a corresponding closing bracket in the correct order, otherwise `stack` contains the unmatched opening brackets.
    return not stack
    #The program returns True if the `stack` is empty (meaning all brackets are matched correctly), or False if the `stack` contains unmatched opening brackets
#Overall this is what the function does:The function `func_1` accepts a string `expression` containing only parentheses (`(`, `)`), curly braces (`{`, `}`), and square brackets (`[`, `]`). It uses a stack to track opening brackets and checks if every opening bracket has a corresponding closing bracket in the correct order. If the stack is empty at the end of the iteration, it means all brackets are matched correctly, and the function returns `True`. Otherwise, if the stack is not empty, indicating unmatched opening brackets, the function returns `False`. The function handles the following cases:
- Returns `False` if the stack is not empty at the end of the iteration, indicating unmatched opening brackets.
- Returns `True` if the stack is empty, indicating all brackets are matched correctly.
Potential edge cases include:
- An empty string `expression` will result in an empty stack, and thus the function will return `True`.
- A string with mismatched or unbalanced brackets will leave unmatched opening brackets in the stack, causing the function to return `False`.

