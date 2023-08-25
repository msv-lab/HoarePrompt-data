n, r = map(int, input().split())
a = list(map(int, input().split()))

def count_heaters(n, r, a):
    heaters = 0
    last = -1

    i = n - 1  # Start searching backward from the end

    while i >= 0:
        if a[i] == 1:
            if i - r + 1 <= last:
                last = i + r - 1
                heaters += 1
            else:
                break
        i -= 1

    if last < n - 1:
        print(-1)  # Not all positions can be heated
    else:
        print(heaters)

count_heaters(n, r, a)