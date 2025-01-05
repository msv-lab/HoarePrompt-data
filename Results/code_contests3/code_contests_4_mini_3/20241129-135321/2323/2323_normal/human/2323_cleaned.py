a = int(input())
b = int(input())
c = 0
copya = a
while copya:
    copya //= 10
    c += 1
ans = a % b
for i in range(c):
    if a % 10 != 0:
        h = a % 10
        a //= 10
        a = 10 ** c * h + a
        ans = min(ans, a % b)
    else:
        h = a % 10
        a //= 10
        a = 10 ** c * h + a
print(ans)