N = int(input())
difficulties = list(map(int, input().split()))

max_difficulty = max(difficulties)
min_difficulty = min(difficulties)

count = 0
if max_difficulty == min_difficulty:
    count = 1
else:
    for K in range(min_difficulty + 1, max_difficulty + 1):
        num_ARC = sum([d >= K - 1 for d in difficulties])
        num_ABC = N - num_ARC
        if num_ARC == num_ABC:
            count += 1

print(count)