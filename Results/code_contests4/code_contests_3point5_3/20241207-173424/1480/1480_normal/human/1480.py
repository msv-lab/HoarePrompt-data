a, b, x = map(int, raw_input().split(" "))

if x > 1 and a == 1:
    s = '1'
    b -= 1
else:
    s = '0'
    a -= 1

while x > 1:
    if s[-1] == '0':
        s += '1'
        b -= 1
    else:
        s += '0'
        a -= 1

    x -= 1

if s[-1] == '0':
    s += '1'*b
    s += '0'*a
else:
    s += '0'*a
    s += '1'*b


print(s)
