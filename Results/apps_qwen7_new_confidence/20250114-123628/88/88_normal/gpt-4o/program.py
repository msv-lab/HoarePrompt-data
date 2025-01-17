def number_of_columns(m, d):
    # Days in each month for a non-leap year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Number of days in the given month
    days = days_in_month[m - 1]
    
    # Days in the first week
    days_in_first_week = 8 - d
    
    # Remaining days after the first week
    remaining_days = days - days_in_first_week
    
    # Number of full weeks needed for the remaining days
    full_weeks = (remaining_days + 6) // 7
    
    # Total columns (weeks) needed
    total_columns = 1 + full_weeks
    
    return total_columns

# Read input
m, d = map(int, input().split())

# Get the result
result = number_of_columns(m, d)

# Print the result
print(result)
