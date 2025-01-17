n = int(input())
s = input()
stack = []
res = []
for c in s:
    if c == '[':
        stack.append(c)
    else:
        stack.pop()
        if stack:
            res.append(stack[-1] + c)
        else:
            res.append(c)
height = len(stack) + 1
for i in range(height):
    line = ''
    for r in res:
        if i == 0 or i == height - 1:
            line += '+-' if r == '[' else '-+'
        else:
            line += '| ' if r == '[' else ' |'
        if i == len(stack):
            line += ' '
    print(line)
