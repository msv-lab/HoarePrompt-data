n = int(input())
ids = list(map(int, input().split()))

count = {}
for i in ids:
    if i != 0:
        count[i] = count.get(i, 0) + 1

for _, c in count.items():
    if c > 2:
        print(-1)
        exit()

pairs = 0
for _, c in count.items():
    if c == 2:
        pairs += 1

print(pairs)