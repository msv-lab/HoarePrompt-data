s = input()

stack = []
for char in s:
    if char == '0':
        stack.append('0')
    elif char == '1':
        stack.append('1')
    else:
        if len(stack) > 0:
            stack.pop()

result = ''.join(stack)
print(result)