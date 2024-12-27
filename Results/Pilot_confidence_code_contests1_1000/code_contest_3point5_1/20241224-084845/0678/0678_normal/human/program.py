import sys
# sys.stdin = open('input.txt')
n = int(raw_input())
a = raw_input().split()
if '0' in a:
    sys.stdout.write('0')
    exit()
zc = 0
hasBad = False
for x in a:
    f = True
    c = 0
    c1 = 0
    for ch in x:
        if ch == '0':
            c += 1
        if ch == '1':
            c1 += 1
        if (ch != '1' and ch != '0') or c1 > 1:
            f = False
            break
    if f:
        zc += c
    else:
        hasBad = True
        sys.stdout.write(x)
if not hasBad:
    sys.stdout.write('1')
sys.stdout.write('0' * zc)
