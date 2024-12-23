n = int(input())
position = 0  # Start at the North Pole

valid = True

for _ in range(n):
    t, dir = input().split()
    t = int(t)
    
    if dir == "North":
        if position - t < 0:
            valid = False
        position -= t
    elif dir == "South":
        if position + t > 20000:
            valid = False
        position += t
    elif dir in ("West", "East"):
        if position == 0 or position == 20000:
            valid = False
    
    if position < 0 or position > 20000:
        valid = False

if position != 0:
    valid = False

if valid:
    print("YES")
else:
    print("NO")
