n, r = map(int, input().split())
a = list(map(int, input().split()))

def count_heaters(n, r, a):
    heaters = 0
    last_heater = -1
    i = n - 1

    # Check if it is possible to heat up the whole house
    while i >= 0:
        if a[i] == 1:
            if i - r + 1 <= last_heater:
                i -= 1
                continue
            heaters += 1
            last_heater = i - r + 1
            i = last_heater - 1

        i -= 1

    if last_heater == -1:
        print(-1)
    else:
        print(heaters)

count_heaters(n, r, a)