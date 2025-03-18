s = input().strip()
print(func_1(s))

def func_1(s):
    n = len(s)
    balance = 0
    positions = []
    for (i, char) in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        positions.append((balance, i, char))
    positions.sort(key=lambda x: (x[0], -x[1]))
    result = ''.join([char for (_, _, char) in positions])
    return result

