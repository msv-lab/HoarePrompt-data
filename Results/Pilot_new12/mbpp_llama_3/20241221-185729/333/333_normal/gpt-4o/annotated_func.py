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
        
    #State of the program after the  for loop has been executed: `expr` is a string containing parentheses, brackets, or braces, `matching_pairs` is a dictionary with keys ')', ']', and '}' and values '(', '[', and '{' respectively, `stack` contains the unmatched opening brackets in `expr`, and `char` is the last character in `expr` if `expr` is not empty.
    return stack == []
    #The program returns True if all brackets in `expr` are properly matched and closed, False otherwise
#Overall this is what the function does:The function accepts a string parameter `expr` containing parentheses, brackets, or braces, and returns a boolean value indicating whether all brackets in `expr` are properly matched and closed. If the string is empty or all brackets are correctly matched and closed, the function returns `True`. Otherwise, it returns `False`, covering cases such as unmatched opening or closing brackets, or brackets that are not properly nested. The function handles various edge cases, including empty strings, strings with only opening or closing brackets, and strings with mixed types of brackets. After the function concludes, the state of the program is that the input string `expr` remains unchanged, and a boolean result is returned indicating the validity of the bracket matching in the input string.

