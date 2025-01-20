(a1, b1) = map(int, input().split())
(a2, b2) = map(int, input().split())
(a3, b3) = map(int, input().split())
if max(a1, b1) >= max(a2, b2) and min(a1, b1) >= min(a2, b2):
    if max(a1, b1) >= max(a3, b3) and min(a1, b1) >= min(a3, b3):
        print('YES')
    else:
        print('NO')
elif max(a1, b1) >= max(a3, b3) and min(a1, b1) >= min(a3, b3):
    print('YES')
else:
    print('NO')