n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x)
b = []
count = 0
for i in range(n):
    if a[i] % 2 == 0:
        b.append(a[i] / 2)
    if a[i] % 2 != 0:
        count = count + 1
        if count % 2 == 1:
            a[i] = a[i] / 2
            b.append(a[i])
        if count % 2 == 0:
            a[i] = a[i] / 2 + 1
            b.append(a[i])
print(b)