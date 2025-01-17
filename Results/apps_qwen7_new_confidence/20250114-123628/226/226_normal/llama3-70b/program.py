a1, a2, a3, a4 = map(int, input().split())
total = a1 + a2 + a3 + a4
if total % 2 == 0:
    half = total // 2
    if (a1 + a2 == half or a1 + a3 == half or a1 + a4 == half or
        a2 + a3 == half or a2 + a4 == half or a3 + a4 == half):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
