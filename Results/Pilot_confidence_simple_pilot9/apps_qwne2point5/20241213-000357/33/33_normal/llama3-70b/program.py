n = int(input())
curr_lat = 90
for _ in range(n):
    t, dir = input().split()
    t = int(t)
    if dir == "North":
        curr_lat += t / 111.195
    elif dir == "South":
        curr_lat -= t / 111.195
    else:
        continue
    if curr_lat < -90 or curr_lat > 90:
        print("NO")
        exit()
    if curr_lat == -90 and dir != "North":
        print("NO")
        exit()
    if curr_lat == 90 and dir != "South":
        print("NO")
        exit()
print("YES" if curr_lat == 90 else "NO")
