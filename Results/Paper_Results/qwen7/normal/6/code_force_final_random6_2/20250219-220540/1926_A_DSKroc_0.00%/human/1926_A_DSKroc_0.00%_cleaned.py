t = int(input())
for q in range(t):
    ac = 0
    bc = 0
    s = input()
    for i in s:
        if i == 'A':
            ac += 1
        else:
            bc += 1
if ac > bc:
    print('A')
else:
    print('B')