s = input()
c = 0
for i, a in enumerate(s):
    if i % 2 == 0 and a == '0':
        c += 1
    if i % 2 == 1 and a == '1':
        c += 1
print(min(c, len(s)-c))