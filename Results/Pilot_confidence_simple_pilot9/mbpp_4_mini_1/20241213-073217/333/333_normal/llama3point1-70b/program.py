def check_expression(expression: str) -> bool:
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}
    
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return not stack
