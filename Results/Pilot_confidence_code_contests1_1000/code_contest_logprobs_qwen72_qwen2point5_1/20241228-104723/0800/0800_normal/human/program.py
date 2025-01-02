rp, crust = map(int, raw_input().split())
n = int(raw_input())

result = 0

lower_bound = rp - crust
upper_bound = rp

lower_bound_sq = (rp - crust) ** 2
upper_bound_sq = rp ** 2

for i in range(n):
    x, y, rs = map(int, raw_input().split())
    ds = x*x + y*y
    #print(x, y, rs, ds)
    if ds < lower_bound_sq or ds > upper_bound_sq:
        # the center is not inside the crust
        continue
    d_lower = int(ds**0.5)
    if d_lower ** 2 == ds:
        # full square
        if d_lower - rs >= lower_bound and d_lower + rs <= upper_bound:
            result += 1
        continue
    l_estimate = 2 * rs * d_lower
    h_estimate = 2 * rs * d_lower + 1
    rs_sq = rs * rs

    if ds + rs_sq - l_estimate >= lower_bound_sq and \
       ds + rs_sq + l_estimate <= upper_bound_sq:
        result += 1

print(result)
