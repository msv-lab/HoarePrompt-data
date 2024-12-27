import sys
l = sys.stdin.readlines()
t = []
for s in l[1:]:
    t.append(s.split())

left = -1 * (2 * 10**9)
right = 2 * 10**9
for c in t:
    if c[2] == 'N':
        if(c[0] == '>'):
            c[0] = '<='
        elif(c[0] == '<'):
            c[0] = '>='
        elif(c[0] == '>='):
            c[0] = '<'
        elif(c[0] == '<='):
            c[0] = '>'

    if(c[0] == '>'):
        if(int(c[1]) >= left):
            left = int(c[1])+1
    elif(c[0] == '<'):
        if(int(c[1]) <= right):
            right = int(c[1])-1
    elif(c[0] == '>='):
        if(int(c[1]) > left):
            left = int(c[1])
    elif(c[0] == '<='):
        if(int(c[1]) < right):
            right = int(c[1])

    if(left > right):
        print('Impossible')
        sys.exit(0)

print(left)