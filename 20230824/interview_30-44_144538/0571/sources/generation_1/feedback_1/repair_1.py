def replace_question_marks(length, s):
    stack = []
    result = list(s)

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                result[i] = "?" 
    
    while stack:
        index = stack.pop()
        result[index] = "?"
    
    count = 0
    for i, char in enumerate(result):
        if char == "?":
            count += 1
            result[i] = "(" if count % 2 == 1 else ")"
    
    count = 0
    for char in result:
        if char == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            return ":("
    
    return "".join(result)

length = int(input())
s = input()
result = replace_question_marks(length, s)
print(result)