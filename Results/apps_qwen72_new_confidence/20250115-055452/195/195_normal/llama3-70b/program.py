n, a, b = map(int, input().split())
t = list(map(int, input().split()))
a_count, b_count, denied = a, b, 0
for i in t:
    if i == 1:
        if a_count > 0:
            a_count -= 1
        elif b_count > 0:
            b_count -= 1
        else:
            denied += 1
    else:
        if b_count > 0:
            b_count -= 1
        else:
            denied += 2
print(denied)
