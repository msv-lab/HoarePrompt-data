n = int(input())
episodes = list(map(int, input().split()))

pairs = 0

for i in range(n):
    for j in range(i+1, n):
        if episodes[i] == episodes[j]:
            pairs += 1

print(pairs)