n, k = map(int, input().split())

problems = []
for _ in range(n):
    problems.append(list(map(int, input().split())))

# Check if there is any team that knows all problems
knows_all = False
for team in problems:
    if sum(team) == n:
        knows_all = True

if knows_all:
    print("NO")
else:
    print("YES")