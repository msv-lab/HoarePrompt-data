n, r = map(int, input().split())
a = list(map(int, input().split()))

def count_heaters(n, r, a):
    heaters = 0
    last_heater = 0
    i = 0

    # Check if it is possible to heat up the whole house
    while i < n:
        if a[i] == 1:
            if i + r - 1 >= n:
                print(-1)
                return
            heaters += 1
            last_heater = i
            i += r

        elif i - r + 1 > last_heater:
            print(-1)
            return
        else:
            i += 1

    print(heaters)

count_heaters(n, r, a)