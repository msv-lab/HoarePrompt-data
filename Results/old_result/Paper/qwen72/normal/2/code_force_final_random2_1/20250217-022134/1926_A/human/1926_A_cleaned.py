t = int(input())
for i in range(t):
    a = input()
    l = 0
    h = 0
    for j in a:
        if j == 'A':
            l += 1
        else:
            h += 1
    if l > h:
        print('A')
    else:
        print('B')