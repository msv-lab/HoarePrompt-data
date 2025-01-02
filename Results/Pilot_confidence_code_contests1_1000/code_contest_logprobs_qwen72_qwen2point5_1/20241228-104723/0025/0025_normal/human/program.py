import sys

def fail():
    print('Impossible')
    sys.exit()

line = raw_input().strip()
parts = line.split()
n = int(parts[-1])
plus = (line.count('+') + 1) * [ n ]
minus = line.count('-') * [ 1 ]
x = sum(plus) - sum(minus) - n
if x < 0:
    fail()
for i, value in enumerate(plus):
    if x == 0:
        break
    delta = min(n - 1, x)
    plus[i] -= delta
    x -= delta
for i, value in enumerate(minus):
    if x == 0:
        break
    delta = min(n - 1, x)
    minus[i] += delta
    x -= delta
if x > 0:
    fail()

if False:
    print(n)
    print(plus)
    print(minus)
    print(x)
parts[0] = str(plus[0])
plus_pos = 1
minus_pos = 0
for i in range(1, len(parts) - 2, 2):
    if parts[i] == '-':
        parts[i + 1] = str(minus[minus_pos])
        minus_pos += 1
    else:
        parts[i + 1] = str(plus[plus_pos])
        plus_pos += 1
print(' '.join(parts))
