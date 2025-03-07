t = int(input())
for _ in range(t):
    (n, f, k) = map(int, input().split())
    a = list(map(int, input().split()))
    favorite_value = a[f - 1]
    same_value_count = 0
    for value in a:
        if value == favorite_value:
            same_value_count += 1
    greater_count = 0
    for value in a:
        if value > favorite_value:
            greater_count += 1
    if greater_count >= k:
        print('YES')
    elif greater_count + same_value_count <= k:
        print('NO')
    else:
        print('MAYBE')