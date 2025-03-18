#State of the program right berfore the function call: expression is a string containing only parentheses ('(', ')'), square brackets ('[', ']'), and curly braces ('{', '}').
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: `expression` is a string containing only parentheses, square brackets, and curly braces, `stack` is empty or contains a sequence of opening brackets that correspond to the correct order of closing brackets, `brackets` is {'(': ')', '{': '}', '[': ']'}. If the loop completes without returning False, the `expression` is correctly matched with no unmatched opening or closing brackets, and `stack` will be empty. Otherwise, if the loop returns False, the `expression` is incorrectly matched, and `stack` will contain unmatched opening brackets.
    return not stack
    #The program returns True if the `stack` is empty, indicating that the `expression` is correctly matched with no unmatched opening or closing brackets; otherwise, it returns False.
#Overall this is what the function does:The function `func_1` accepts a string `expression` containing only parentheses (`(`, `)`), square brackets (`[`, `]`), and curly braces (`{`, `}`) and returns `True` if the expression has correctly matched opening and closing brackets, and `False` otherwise. The function uses a stack to keep track of opening brackets and ensures that each opening bracket has a corresponding closing bracket in the correct order. If the stack is empty at the end of the iteration, it means all brackets are correctly matched; otherwise, it means there are unmatched opening brackets, resulting in a return value of `False`.

