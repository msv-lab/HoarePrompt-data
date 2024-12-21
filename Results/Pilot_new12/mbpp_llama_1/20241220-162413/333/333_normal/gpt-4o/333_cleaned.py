def func_1(expr):
    stack = []
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        if char in matching_pairs.values():
            stack.append(char)
        elif char in matching_pairs:
            if stack == [] or stack.pop() != matching_pairs[char]:
                return False
    return stack == []
assert func_1('{()}[{}]') == True
assert func_1('{()}[{]') == False
assert func_1('{()}[{}][]({})') == True