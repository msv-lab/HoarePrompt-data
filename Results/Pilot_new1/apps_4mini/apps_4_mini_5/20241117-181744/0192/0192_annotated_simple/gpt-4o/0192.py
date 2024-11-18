x, y = map(int, input().split())

# The minimum number of seconds required to transform the triangle of side length x to side length y
# can be computed as (x - y) / 2 plus the remainder when (x - y) is divided by 2.
# This is because we can decrease each side by 1 in each second, and for each decrease of 1, we can
# reduce the total side lengths by 3. So we need (x - y) // 2 steps to reduce two sides in each step
# and one additional step if there is a remainder.

print((x - y) // 2 + (x - y) % 2)
