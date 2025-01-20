# Read input values
a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

# Calculate the deficit/surplus for each color
deficit_blue = max(0, x - a)
deficit_violet = max(0, y - b)
deficit_orange = max(0, z - c)

# Calculate how many extra spheres we have
extra_blue = max(0, a - x)
extra_violet = max(0, b - y)
extra_orange = max(0, c - z)

# Each surplus sphere can potentially be used to create another sphere
# Transforming two surplus spheres into one needed sphere
# Thus, the number of effective extra spheres is half of the surplus count (integer division)
extra_spheres = (extra_blue // 2) + (extra_violet // 2) + (extra_orange // 2)

# Calculate the total deficit
total_deficit = deficit_blue + deficit_violet + deficit_orange

# Check if the total surplus is enough to cover the total deficit
if extra_spheres >= total_deficit:
    print("Yes")
else:
    print("No")
