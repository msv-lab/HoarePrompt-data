t = int(input())
for _ in range(t):
    (n, f, k) = map(int, input().split())
    a = list(map(int, input().split()))
    favorite_value = a[f - 1]
    sorted_a = sorted(a, reverse=True)
    removed_count = 0
    for i in range(k):
        if sorted_a[i] == favorite_value:
            removed_count += 1
    favorite_count = sorted_a.count(favorite_value)
    if removed_count == favorite_count:
        print('YES')
    elif removed_count == 0:
        print('NO')
    else:
        print('MAYBE')