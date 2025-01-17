def generate_unlucky_years(x, y, l, r):
    # Generate all unlucky years within a certain reasonable bound.
    unlucky_years = set()
    a, b = 0, 0
    max_value = r + 1
    power_x = 1
    while power_x < max_value:
        power_y = 1
        b = 0
        while power_x + power_y < max_value:
            year = power_x + power_y
            if l <= year <= r:
                unlucky_years.add(year)
            power_y *= y
            b += 1
            if power_y > r:
                break
        power_x *= x
        a += 1
        if power_x > r:
            break
    return unlucky_years

def max_golden_age(x, y, l, r):
    unlucky_years = generate_unlucky_years(x, y, l, r)
    unlucky_years = sorted(list(unlucky_years))
    
    max_length = 0
    previous_end = l - 1
    
    for year in unlucky_years:
        if year > previous_end + 1:
            max_length = max(max_length, year - previous_end - 1)
        previous_end = year
    
    if previous_end < r:
        max_length = max(max_length, r - previous_end)
    
    return max_length

# Read input values
x, y, l, r = map(int, input().split())

# Calculate and print the maximum length of the golden age
print(max_golden_age(x, y, l, r))
