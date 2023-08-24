n = int(input())
difficulties = list(map(int, input().split()))

max_problems = 1
current_problems = 1

for i in range(1, n):
    if difficulties[i] <= difficulties[i-1] * 2:
        current_problems += 1
    else:
        current_problems = 1
    
    max_problems = max(max_problems, current_problems)

print(max_problems)