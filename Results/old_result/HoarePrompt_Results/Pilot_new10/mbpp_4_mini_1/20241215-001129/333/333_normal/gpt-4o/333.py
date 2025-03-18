def check_expression(expr):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expr:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False
    return stack == []

# Testing the function with the provided test cases
assert check_expression("{()}[{}]") == True
assert check_expression("{()}[{]") == False
assert check_expression("{()}[{}][]({})") == True
