n, m, k = map(int, input().split())
filters = list(map(int, input().split()))

filters.sort(reverse=True)  # sort filters in descending order

sockets = k  # number of available sockets
filters_needed = 0  # number of filters needed
i = 0  # index for iterating through filters

# iterate through filters and check if devices can be plugged
while i < n and sockets < m:
    sockets += filters[i] - 1  # add sockets from filter
    filters_needed += 1  # increment number of filters needed
    i += 1

if sockets < m:
    print(-1)  # not enough sockets for all devices
else:
    print(filters_needed)  # minimum number of filters needed