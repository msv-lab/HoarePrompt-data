N = int(input())
difficulties = list(map(int, input().split()))

max_difficulty = max(difficulties)
min_difficulty = min(difficulties)

count = 0
for K in range(min_difficulty, max_difficulty + 1):
    num_ARC = sum([d >= K for d in difficulties])
    num_ABC = sum([d < K for d in difficulties])
    if num_ARC == num_ABC:
        count += 1

print(count)