#State of the program right berfore the function call: expr is a string consisting of parentheses and/or other characters.
def func_1(expr):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False
        
    #State of the program after the  for loop has been executed: `expr` is an empty string or has been fully processed, `matching_pairs` remains `{')': '(', ']': '[', '}': '{'}`, and `stack` is empty if all brackets in `expr` were matched; otherwise, `stack` contains the unmatched opening brackets from the original string `expr`.
    return stack == []
    #The program returns True if all brackets in `expr` were matched, False otherwise
#Overall this is what the function does:The function accepts a string parameter `expr` and checks if all brackets in `expr` are properly matched. It returns `True` if all brackets are matched and `False` otherwise. The function handles strings containing parentheses `()`, square brackets `[]`, and curly brackets `{}`, and it correctly identifies mismatched or unmatched brackets. The function's return value indicates whether the input string has a valid bracket sequence, with `True` indicating a valid sequence and `False` indicating an invalid sequence. The function does not modify the input string `expr` and does not perform any error handling for non-string inputs or strings containing invalid characters.

