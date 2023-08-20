n = int(input())
difficulties = list(map(int, input().split()))

valid_contests = 0

for i in range(n):
    for j in range(i, n):
        is_valid_contest = True
        for k in range(i, j+1):
            if difficulties[k] > difficulties[i] * 2:
                is_valid_contest = False
                break
        if is_valid_contest:
            valid_contests = max(valid_contests, j - i + 1)

print(valid_contests)