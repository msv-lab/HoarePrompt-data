n, s = map(int, input().split())
mugs = list(map(int, input().split()))

# Sort the mugs in increasing order of volume
mugs.sort()

# Calculate the total volume of all mugs except the largest one
total_volume = sum(mugs[:-1])

# If the total volume is less than or equal to the cup volume, the friends can play without anyone losing
if total_volume <= s:
    print("YES")
else:
    print("NO")