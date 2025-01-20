l1, r1, l2, r2, k = map(int, input().split())

# Calculate the intersection of Sonya's and Filya's time segments
start = max(l1, l2)
end = min(r1, r2)

# If Sonya prinks during their common time, subtract 1 minute
if start <= k <= end:
    end -= 1

# Calculate the number of minutes they can spend together
minutes_together = max(0, end - start + 1)

print(minutes_together)
