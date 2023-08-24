# Read input
n, m = map(int, input().split())
coffee = list(map(int, input().split()))

# Sort the coffee cups in descending order of caffeine dosage
coffee.sort(reverse=True)

# Initialize variables
pages_written = 0
days = 0

# Keep track of the minimum caffeine dosage needed to write the remaining pages
min_caffeine = float('inf')

# Iterate through each cup of coffee
for caffeine in coffee:

    # Calculate the number of pages that can be written with the current cup of coffee
    pages = max(0, caffeine - (days - 1))

    # Update the minimum caffeine dosage needed
    min_caffeine = min(min_caffeine, caffeine - (days - 1))

    # Update the number of pages written and the number of days
    pages_written += pages
    days += 1

    # Check if all pages have been written
    if pages_written >= m + days:
        break

# Check if it is possible to write the coursework
if pages_written + (n - days) + m + 1 < m:
    print(-1)
else:
    print(min_caffeine)