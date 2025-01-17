def func_1(m, x, costs):
    costs.sort(reverse=True)
    earnings = 0
    happiness = []
    for i in range(1, m + 1):
        earnings += x
        while costs and costs[-1] <= earnings:
            earnings -= costs[-1]
            happiness.append(1)
            costs.pop()
    return len(happiness)
t = int(input())
for _ in range(t):
    (m, x) = map(int, input().split())
    costs = list(map(int, input().split()))
    print(func_1(m, x, costs))