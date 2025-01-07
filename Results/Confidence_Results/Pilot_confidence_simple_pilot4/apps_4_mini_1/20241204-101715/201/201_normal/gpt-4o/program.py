# Read input values
h1, h2 = map(int, input().split())
a, b = map(int, input().split())

# Calculate the initial height difference
height_diff = h2 - h1

# If the caterpillar reaches or surpasses the apple location in the first day
if a * 12 >= height_diff:
    print(0)
    exit()

# If the caterpillar slips down more or equal to what it climbs up in a full day-night cycle
if a <= b:
    print(-1)
    exit()

# Calculate the effective climb per day (considering 12 hours up and 12 hours sliding down)
effective_climb_per_day = (a * 12) - (b * 12)

# Calculate the total effective climbs required (after the first day)
remaining_diff = height_diff - (a * 12)
days_needed = (remaining_diff + effective_climb_per_day - 1) // effective_climb_per_day

# Output the number of days
print(days_needed + 1)
