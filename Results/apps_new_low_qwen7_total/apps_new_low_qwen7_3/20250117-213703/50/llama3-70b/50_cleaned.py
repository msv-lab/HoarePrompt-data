k = int(input())
n = 1
while True:
    s = str(n)
    if len(s) >= k:
        print(s[k - 1])
        break
    k -= len(s)
    n += 1