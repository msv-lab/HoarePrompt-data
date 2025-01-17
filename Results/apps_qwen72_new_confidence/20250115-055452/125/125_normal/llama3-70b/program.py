x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

if x > a:
    print("NO")
elif y > a + b:
    print("NO")
elif z > a + b + c:
    print("NO")
else:
    print("YES")
