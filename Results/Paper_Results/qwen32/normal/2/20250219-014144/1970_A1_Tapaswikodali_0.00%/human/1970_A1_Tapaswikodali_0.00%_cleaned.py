s = input()
balance = 0
details = []
for (i, char) in enumerate(s):
    if char == '(':
        balance += 1
    else:
        balance -= 1
    details.append((balance, -i, char))
details.sort()
result = ''.join((char for (_, _, char) in details))
print(result)