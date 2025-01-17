def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def check_consecutive_months(n, a):
    common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Extend the months array to cover cases that span over the end and start of a year
    months = leap_year + common_year + leap_year + common_year
    
    for i in range(len(months) - n + 1):
        if months[i:i+n] == a:
            return "YES"
    return "NO"

# Reading input
n = int(input())
a = list(map(int, input().split()))

# Checking the sequence
result = check_consecutive_months(n, a)
print(result)
