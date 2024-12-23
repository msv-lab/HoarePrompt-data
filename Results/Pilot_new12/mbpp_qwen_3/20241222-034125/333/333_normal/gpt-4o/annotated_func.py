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
        
    #State of the program after the  for loop has been executed: `expr` is a string consisting of parentheses, square brackets, and curly braces, `stack` is either an empty list or a list containing the unmatched opening brackets, and `matching_pairs` is {')': '(', ']': '[', '}': '{'}. If `expr` contains all correctly matched pairs, `stack` will be an empty list after the loop completes. If there are any unmatched closing brackets in `expr`, `stack` will contain the corresponding unmatched opening brackets.
    return stack == []
    #`The program returns True if 'stack' is an empty list, indicating all brackets in 'expr' are correctly matched, or False if 'stack' contains unmatched opening brackets`
#Overall this is what the function does:The function `func_1` accepts a string `expr` consisting of parentheses ('(', ')'), square brackets ('[', ']'), and curly braces ('{', '}'). It checks if all the opening brackets in `expr` have correctly matched closing brackets. The function uses a stack to keep track of unmatched opening brackets. After iterating through the string, if the stack is empty, it means all brackets are correctly matched, and the function returns `True`. Otherwise, it returns `False`. This includes cases where there are unmatched opening brackets left in the stack, indicating incorrect matching, and thus returning `False`.

