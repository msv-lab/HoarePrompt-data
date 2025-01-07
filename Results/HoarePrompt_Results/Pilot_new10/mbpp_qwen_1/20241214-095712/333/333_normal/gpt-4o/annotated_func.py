#State of the program right berfore the function call: expr is a string containing only parentheses, i.e., '(', ')', square brackets, i.e., '[', ']', and curly braces, i.e., '{', '}'.
def func_1(expr):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False
        
    #State of the program after the  for loop has been executed: `expr` is a string containing only parentheses, square brackets, and curly braces, `stack` is either an empty list or a list of opening brackets in the order they were encountered, `matching_pairs` is {')': '(', ']': '[', '}': '{'}. If `expr` is a valid sequence of nested and properly matched parentheses, square brackets, and curly braces, the `stack` will be empty at the end of the loop. Otherwise, the `stack` will contain unmatched opening brackets.
    return stack == []
    #The program returns True if the stack is empty, indicating that `expr` is a valid sequence of nested and properly matched parentheses, square brackets, and curly braces; otherwise, it returns False.
#Overall this is what the function does:The function accepts a string `expr` and returns `True` if `expr` is a valid sequence of nested and properly matched parentheses, square brackets, and curly braces; otherwise, it returns `False`.

