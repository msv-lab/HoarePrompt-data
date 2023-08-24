n, m = map(int, input().split())

bulbs = set(range(1, m+1))
switches = [set(map(int, input().split()[1:])) for _ in range(1, n+1)]

for switch in switches:
    bulbs = bulbs.intersection(switch)
    if len(bulbs) == m:
        break

if len(bulbs) == m:
    print("YES")
else:
    print("NO")