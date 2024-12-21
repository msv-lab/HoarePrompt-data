#State of the program right berfore the function call: expr is a string consisting of parentheses ('(', ')'), square brackets ('[', ']'), and curly braces ('{', '}').
def func_1(expr):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False
        
    #State of the program after the  for loop has been executed: `expr` is a string consisting of parentheses, square brackets, and curly braces, `stack` is a list that is either empty (if the expression is valid) or contains the unmatched opening symbols in reverse order (if the expression is invalid), and `char` is the last character in `expr`.
    return stack == []
    #The program returns True if the stack is empty, indicating the expression is valid, or False if the stack is not empty, indicating the expression is invalid
#Overall this is what the function does:The function `func_1` accepts a parameter `expr`, a string consisting of parentheses ('(', ')'), square brackets ('[', ']'), and curly braces ('{', '}'). It checks whether the expression is balanced, meaning that every opening symbol has a corresponding closing symbol and the pairs of symbols are properly nested. The function uses a stack to keep track of unmatched opening symbols. After iterating through the string, the function returns `True` if the stack is empty (indicating the expression is valid), otherwise it returns `False` (indicating the expression is invalid). The function covers all possible edge cases where the expression can be valid or invalid, including scenarios where there are unmatched opening symbols, mismatched pairs, or incomplete pairs.

