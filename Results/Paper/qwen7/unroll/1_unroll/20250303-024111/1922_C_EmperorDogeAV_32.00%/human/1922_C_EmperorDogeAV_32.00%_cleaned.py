t = int(input())

def func_1(cities, n):
    prog_cities = [0] * (n - 1)
    for i in range(n - 1):
        back = -99999999
        forward = 99999999
        if i > 0:
            back = cities[i - 1]
        if i < n - 1:
            forward = cities[i + 1]
        if abs(forward - cities[i]) < abs(cities[i] - back):
            prog_cities[i] = 1
        else:
            prog_cities[i] = abs(forward - cities[i])
    return prog_cities
for _ in range(t):
    n = int(input())
    cities = input().split()
    for i in range(n):
        cities[i] = int(cities[i])
    forward_cities = func_1(cities, n)
    cities.reverse()
    backward_cities = func_1(cities, n)
    pref_sum_f = [0]
    pref_sum_b = [0]
    for i in range(n - 1):
        pref_sum_f.append(pref_sum_f[i] + forward_cities[i])
        pref_sum_b.append(pref_sum_b[i] + backward_cities[i])
    pref_sum_b.reverse()
    m = int(input())
    for i in range(m):
        (a, b) = input().split()
        (a, b) = (int(a), int(b))
        if a < b:
            print(pref_sum_f[b - 1] - pref_sum_f[a - 1])
        else:
            print(pref_sum_b[b - 1] - pref_sum_b[a - 1])