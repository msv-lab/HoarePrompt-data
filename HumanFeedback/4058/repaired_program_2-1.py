n, r = map(int, input().split())
a = list(map(int, input().split()))

def count_heaters(n, r, a):
    heaters = 0
    last_heater = -1
    i = n - 1

    while i >= 0:
        if a[i] == 1:
            if i - r + 1 <= last_heater:
                i -= r
                continue
            heaters += 1
            last_heater = i - r + 1
            i -= r
        else:
            i -= 1

    if last_heater < 0:
        print(-1)
    else:
        print(heaters)

count_heaters(n, r, a)