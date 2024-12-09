#State of the program right berfore the function call: expression is a string that may contain various types of brackets (e.g., '()', '{}', '[]') and any other characters.
def func_1(expression):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
        
    #State of the program after the  for loop has been executed: `stack` is either empty or contains unmatched opening brackets, `expression` is a string that may contain various types of brackets and other characters, and the loop returns False if there is a mismatch between opening and closing brackets. If there are no mismatches, then `stack` is empty (indicating all brackets are matched).
    return not stack
    #The program returns True if all brackets in the 'expression' are matched and the 'stack' is empty; otherwise, it returns False.
#Overall this is what the function does:The function accepts a string `expression` and checks if all types of brackets (parentheses '()', curly braces '{}', and square brackets '[]') are correctly matched and nested. It returns True if all brackets are matched and there are no unmatched opening brackets left; otherwise, it returns False. Additionally, if the expression contains any characters that are not brackets, they are ignored in the matching process.

