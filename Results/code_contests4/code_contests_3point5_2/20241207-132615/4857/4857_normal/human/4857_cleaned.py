x = int(input())
i = 0
k = 1
c = 0
while x - (i + k) >= 0:
    i = i + k
    x = x - i
    c = c + 1
    k = k + 1
print(c)