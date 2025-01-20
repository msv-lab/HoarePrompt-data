(a, b, c) = map(int, input().split())
(x, y, z) = map(int, input().split())
deficit_blue = max(0, x - a)
deficit_violet = max(0, y - b)
deficit_orange = max(0, z - c)
extra_blue = max(0, a - x)
extra_violet = max(0, b - y)
extra_orange = max(0, c - z)
extra_spheres = extra_blue // 2 + extra_violet // 2 + extra_orange // 2
total_deficit = deficit_blue + deficit_violet + deficit_orange
if extra_spheres >= total_deficit:
    print('Yes')
else:
    print('No')