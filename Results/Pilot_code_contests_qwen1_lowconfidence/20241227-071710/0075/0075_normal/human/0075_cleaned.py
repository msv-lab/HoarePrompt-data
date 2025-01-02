a = int(input())
b = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1, 1, 2, 0, 1, 0, 0]
res = 0
if a == 0:
    res += b[0]
while a > 0:
    res += b[a % 16]
    a /= 16
print(res)