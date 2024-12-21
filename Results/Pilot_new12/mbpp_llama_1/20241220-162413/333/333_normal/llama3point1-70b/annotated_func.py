#State of the program right berfore the function call: expression is a string containing parentheses, brackets, or braces.
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: `expression` is a string that has been fully traversed, `brackets` is a dictionary {'(': ')', '{': '}', '[': ']'}, `char` is the last character in the `expression`, and `stack` contains any unmatched opening brackets from the `expression`.
    return not stack
    #The program returns True if the stack is empty (indicating all brackets in the expression were properly matched) and False otherwise (indicating there are unmatched opening brackets in the expression).
#Overall this is what the function does:The function accepts a string parameter `expression` containing parentheses, brackets, or braces and returns a boolean value indicating whether all brackets in the expression are properly matched. If the expression has balanced brackets, the function returns `True`; otherwise, it returns `False`. This includes cases where there are unmatched opening brackets, unmatched closing brackets, or a combination of both. The function handles all potential edge cases, including empty strings, strings with only opening or closing brackets, and strings with properly nested brackets. The return value provides a clear indication of whether the brackets in the input string are balanced, allowing the user to determine the validity of the bracket arrangement in the expression.

