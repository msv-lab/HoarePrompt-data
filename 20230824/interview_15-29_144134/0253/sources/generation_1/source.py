k1, k2, k3 = map(int, input().split())

# To switch on three garlands so that at each second after switching on at least one garland will be lit,
# we need to find a common multiple of the given time intervals.

# The least common multiple (LCM) of three numbers can be calculated using the formula LCM(a, b, c) = LCM(LCM(a, b), c)
lcm_k = k1 * k2 * k3

# If the least common multiple is less than or equal to the maximum time interval among the three garlands,
# it is not possible to switch on the garlands in a way that satisfies the condition
if lcm_k <= max(k1, k2, k3):
    print("NO")
else:
    print("YES")