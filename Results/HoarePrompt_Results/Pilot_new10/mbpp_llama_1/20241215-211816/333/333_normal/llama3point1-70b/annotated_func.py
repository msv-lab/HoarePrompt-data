#State of the program right berfore the function call: expression is a string containing characters that are typically used in expressions, such as parentheses, brackets, and braces.
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: `expression` is the original string containing characters, `char` is the last character in `expression`, `stack` contains unmatched opening brackets if any, and `brackets` is {'(': ')', '{': '}', '[': ']'}
    return not stack
    #The program returns True if there are no unmatched opening brackets in 'stack', otherwise it returns False
#Overall this is what the function does:The function accepts a string `expression` and returns True if all brackets are properly matched and balanced, and False otherwise, considering cases where closing brackets do not match their corresponding opening brackets, or where there are unmatched opening brackets at the end of the string

