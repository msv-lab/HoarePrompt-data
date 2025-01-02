students, num_puzzles = list(map(int, raw_input().split()))
puzzles = list(map(int, raw_input().split()))
puzzles.sort()
best = 999999
for i in range(num_puzzles-students+1):
    best = min(puzzles[i+students - 1] - puzzles[i], best)
if (best == 999999):
    best = puzzles[-1] - puzzles[0]
print(best)