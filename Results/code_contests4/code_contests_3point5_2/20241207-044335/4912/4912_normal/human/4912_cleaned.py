n = int(input())
s = input()
res = []
count = 0
if s[0] == '1':
    one = 1
else:
    one = 0
temp = []
tar = 0
for i in range(1, n - 1):
    if s[i - 1:i + 2] == '101':
        tar = 1
        temp.append(one)
        one = 0
    else:
        if s[i] == '0' and tar == 1:
            temp.append(one)
            res.append(temp.copy())
            temp = []
            tar = 0
        if s[i] == '1':
            one += 1
        else:
            one = 0
if s[-1] == '1':
    one += 1
if tar == 1:
    temp.append(one)
    res.append(temp.copy())
for x in res:
    temp = 0
    m = len(x)
    f = []
    if m == 2:
        temp = max(x[0], x[1])
    if m == 3:
        temp = max(x[0], x[1], x[2])
    if m == 4:
        temp = max(x[0] + x[2], x[3] + max(x[0], x[1]))
    if m >= 5:
        f.append([x[0], x[1]])
        f.append([x[1], max(x[2], x[0])])
        f.append(x[0] + x[2], x[3] + f[0])
        for i in range(3, m - 1):
            f.append(x[i] + max(f[i - 2][0], f[i - 3][0]))
            f.append(x[i + 1] + max(f[i - 2][0], f[i - 2][1]))
        temp = max(f[-1][0], f[-1][1], f[-2][0])
    count += temp
print(count)