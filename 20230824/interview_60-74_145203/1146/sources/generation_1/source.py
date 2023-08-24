n, m = map(int, input().split())

bulbs = set(range(1, m+1))
switches = [set(map(int, input().split()[1:])) for _ in range(n)]

for switch in switches:
    bulbs = bulbs.intersection(switch)
    if len(bulbs) == 0:
        break

if len(bulbs) == 0:
    print("NO")
else:
    print("YES")