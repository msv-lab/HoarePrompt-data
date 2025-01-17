b1, q, l, m = map(int, input().split())
bad = set(map(int, input().split()))

count = 0
while True:
    if abs(b1) > l:
        break
    if b1 not in bad:
        count += 1
    if q == 0:
        break
    b1 *= q

if q == 0 and abs(b1) <= l and b1 not in bad:
    print(1)
elif q == 1 and b1 in bad:
    print(0)
else:
    print("inf" if q == 1 or abs(q) == 1 else count)
