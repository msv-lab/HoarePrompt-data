__author__ = 'RASULBEK'
n = input()
p = map(int, raw_input().split())
i = 0
a = []
while i < n:
    j = 0
    b = []
    s = raw_input()
    while j < len(s):
        if s[j] == '1':
            b.append(1)
        else:
            b.append(0)
        j += 1
    a.append(b)
    i += 1
i = 0
while i < n:
    j = i + 1
    while j < n:
        if p[i] > p[j]:
            if a[i][j] == 1 and a[j][i] == 1:
                tmp = p[i]
                p[i] = p[j]
                p[j] = tmp
        j += 1
    i += 1
i = 0
while i < n:
    j = i + 1
    while j < n:
        if p[i] > p[j]:
            if a[i][j] == 1 and a[j][i] == 1:
                tmp = p[i]
                p[i] = p[j]
                p[j] = tmp
        j += 1
    i += 1
i = 0
s = ''
while i < n:
    s += str(p[i]) + ' '
    i += 1
print(s)