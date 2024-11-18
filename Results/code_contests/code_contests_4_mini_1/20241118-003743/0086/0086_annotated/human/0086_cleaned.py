s = raw_input()
stack = []
for i in xrange(len(s)):
    if len(stack) == 0 or s[i] == 'S':
        stack.append(s[i])
        continue
    if s[i] == 'T':
        if stack[-1] == 'S':
            stack.pop()
        else:
            stack.append(s[i])
print(len(stack))