def func_1(n, t, bus_routes):
    min_wait_time = float('inf')
    chosen_route = -1
    for i in range(n):
        (s_i, d_i) = bus_routes[i]
        if s_i >= t:
            wait_time = s_i - t
        elif (t - s_i) % d_i == 0:
            wait_time = 0
        else:
            wait_time = d_i - (t - s_i) % d_i
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            chosen_route = i + 1
    return chosen_route
input = sys.stdin.read
data = input().split()
n = int(data[0])
t = int(data[1])
bus_routes = []
for i in range(n):
    s_i = int(data[2 + i * 2])
    d_i = int(data[2 + i * 2 + 1])
    bus_routes.append((s_i, d_i))
print(func_1(n, t, bus_routes))