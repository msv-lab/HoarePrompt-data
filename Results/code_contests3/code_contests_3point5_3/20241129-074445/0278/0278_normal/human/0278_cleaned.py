(n, V) = map(int, raw_input().split())
(a, b) = ([float(i) for i in raw_input().split()], [float(i) for i in raw_input().split()])
print(min(reduce(lambda ans, ai: ans + reduce(lambda minx, ab: min(minx, ab[0] / ab[1]), zip(b, a), 2.0 ** 30) * ai, a, 0), V))