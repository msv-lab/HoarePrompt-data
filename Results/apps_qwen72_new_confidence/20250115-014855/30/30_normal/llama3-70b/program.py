s = input()
a = int(s[0]) + int(s[1]) + int(s[2])
b = int(s[3]) + int(s[4]) + int(s[5])

if a == b:
    print(0)
else:
    diff = abs(a - b)
    res = float('inf')
    for i in range(6):
        for j in range(10):
            if i < 3:
                new_a = a - int(s[i]) + j
            else:
                new_a = a
            if i >= 3:
                new_b = b - int(s[i]) + j
            else:
                new_b = b
            if new_a == new_b:
                res = min(res, 1)
            elif abs(new_a - new_b) < diff:
                res = min(res, 1)
    print(res)
