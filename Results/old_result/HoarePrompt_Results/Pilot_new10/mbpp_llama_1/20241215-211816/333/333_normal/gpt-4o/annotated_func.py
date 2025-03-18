#State of the program right berfore the function call: expr is a string containing parentheses, brackets, or braces.
def func_1(expr):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False
        
    #State of the program after the  for loop has been executed: `expr` is the original string containing parentheses, brackets, or braces, `stack` contains all the unmatched opening brackets in `expr`, `matching_pairs` is the original dictionary containing the matching pairs of brackets. If `expr` has matching brackets, `stack` is empty. If `expr` has unmatched closing brackets, the program returned False before finishing all iterations.
    return stack == []
    #The program returns True if `expr` has matching brackets or no brackets, and False if `expr` has unmatched opening brackets.
#Overall this is what the function does:The function accepts a string `expr` containing parentheses, brackets, or braces, and returns True if `expr` has matching brackets or no brackets, and False if `expr` has unmatched opening or closing brackets, or if there are more opening brackets than closing brackets

