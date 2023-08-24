n, k = map(int, input().split())
heights = list(map(int, input().split()))

actions = []
for i in range(n-1):
    diff = k - (heights[i+1] - heights[i])
    if diff > 0:
        actions.append(f"+ {i+2} {diff}")
        heights[i+1] += diff
    elif diff < 0:
        actions.append(f"- {i+2} {abs(diff)}")
        heights[i+1] -= abs(diff)

print(len(actions))
for action in actions:
    print(action)