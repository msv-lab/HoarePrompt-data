l1 = list(map(int, raw_input().split()))
(n, k) = (l1[0], l1[1])
l = raw_input()
mestot = None
mestok = None
for i in range(len(l)):
    if l[i] == 'G':
        mestok = i
    if l[i] == 'T':
        mestot = i
    if mestok != None and mestot != None:
        break
fl = True
if abs(mestot - mestok) % k == 0:
    for i in range(mestok, len(l), k):
        if l[i] == '#':
            fl = False
            break
    if fl != False and mestot < mestok:
        l = l[::-1]
        for i in range(len(l)):
            if l[i] == 'G':
                mestok = i
            if l[i] == 'T':
                mestot = i
        for i in range(mestok, len(l), k):
            if l[i] == '#':
                fl = False
                break
    if fl == True:
        print('YES')
    else:
        print('NO')
else:
    print('NO')