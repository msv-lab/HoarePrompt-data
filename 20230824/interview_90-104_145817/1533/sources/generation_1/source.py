n = int(input())
names = []
for _ in range(n):
    name = input().lower()
    if name in names:
        print("YES")
    else:
        print("NO")
        names.append(name)