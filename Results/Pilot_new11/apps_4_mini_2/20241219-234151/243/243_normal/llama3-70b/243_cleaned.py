m = int(input())
count = 0
n = 1
while True:
    if n // 5 ** count >= m:
        break
    count += 1
n = 1
ans = []
while True:
    if n // 5 ** count < m:
        break
    ans.append(n)
    n += 1
print(len(ans))
print(' '.join(map(str, ans)))