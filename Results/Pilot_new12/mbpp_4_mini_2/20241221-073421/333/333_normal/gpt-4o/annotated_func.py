#State of the program right berfore the function call: expr is a string that may contain parentheses, brackets, and braces.
def func_1(expr):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False
        
    #State of the program after the  for loop has been executed: `stack` is empty if `expr` contains balanced parentheses, brackets, and braces; otherwise, `stack` contains unmatched opening characters.
    return stack == []
    #The program returns True if the stack is empty, indicating that the expression 'expr' contains balanced parentheses, brackets, and braces; otherwise, it returns False, meaning 'stack' contains unmatched opening characters.
#Overall this is what the function does:The function accepts a string parameter `expr` that may contain parentheses `()`, brackets `[]`, and braces `{}`. It checks whether the parentheses, brackets, and braces in the string are balanced. Specifically, it uses a stack to track opening characters, allowing it to match each opening character with its corresponding closing character. The function returns `True` if all characters are matched properly and the stack is empty at the end, indicating that the expression is balanced. If any unmatched characters remain in the stack, or if a closing character does not have a corresponding opening character, it returns `False`. The function does not account for any characters other than the defined parentheses, brackets, and braces, and thus ignores any other symbols in the input string.

