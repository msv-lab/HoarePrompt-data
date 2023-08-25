n, r = map(int, input().split())
a = list(map(int, input().split()))

def count_heaters(n, r, a):
    heaters = 0
    last_heater = -r  # Initialize `last_heater` to a negative value
    i = 0

    # Check if it is possible to heat up the whole house
    while i < n:
        if a[i] == 1:
            # Check if the current heater can cover the position to the right of `last_heater + 1`
            if i - r + 1 > last_heater + 1:
                print(-1)
                return
            heaters += 1
            last_heater = i
            i += r

        else:
            i += 1

    # Check if all the rooms are covered
    if last_heater + r >= n:
        print(heaters)
    else:
        print(-1)

count_heaters(n, r, a)