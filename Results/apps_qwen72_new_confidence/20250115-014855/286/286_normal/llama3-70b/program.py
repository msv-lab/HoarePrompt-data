n = int(input())
x1, x2 = map(int, input().split())
lines = []
for _ in range(n):
    k, b = map(int, input().split())
    lines.append((k, b))

def intersect(line1, line2, x1, x2):
    k1, b1 = line1
    k2, b2 = line2
    if k1 == k2:
        return False
    x = (b2 - b1) / (k1 - k2)
    if x1 < x < x2:
        return True
    return False

for i in range(n):
    for j in range(i + 1, n):
        if intersect(lines[i], lines[j], x1, x2):
            print("YES")
            exit()
print("NO")
