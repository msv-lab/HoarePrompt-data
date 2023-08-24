n, k = map(int, input().split())

problems = []
for _ in range(n):
    problems.append(list(map(int, input().split())))

# Check if there is any team that knows all problems
for team in problems:
    if sum(team) == k:
        print("NO")
        exit()

print("YES")