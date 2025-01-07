#State of the program right berfore the function call: expr is a string that may contain various types of brackets (such as '()', '{}', '[]') which need to be checked for balance.
def func_1(expr):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False
        
    #State of the program after the  for loop has been executed: `expr` is a string that may contain various types of brackets, `stack` is empty if the brackets in `expr` are balanced, otherwise `stack` contains the unmatched opening brackets. If `expr` is empty, `stack` remains empty.
    return stack == []
    #The program returns True if the brackets in 'expr' are balanced (stack is empty), and False if there are unmatched opening brackets (stack is not empty)
#Overall this is what the function does:The function accepts a string `expr` that may contain various types of brackets (parentheses, curly braces, and square brackets) and checks if they are balanced. It returns True if all brackets are correctly matched and closed; otherwise, it returns False. If there are unmatched opening brackets or closing brackets that do not correspond to any opening brackets, the function will also return False.

