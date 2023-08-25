n, r = map(int, input().split())
a = list(map(int, input().split()))

def count_heaters(n, r, a):
    heaters = 0
    last_heater = 0
    i = 0

    # Check if it is possible to heat up the whole house
    while i < n:
        if a[i] == 1:
            if i + r - 1 >= n:  # Check if the coverage exceeds the boundary
                print(-1)
                return
            heaters += 1
            last_heater = i + r - 1  # Fix: Update last_heater to the right of i
            i += r

        elif i - r + 1 > last_heater:  # Check if there is a gap that cannot be covered by any heater
            print(-1)
            return
        else:
            i += 1

    print(heaters)

count_heaters(n, r, a)