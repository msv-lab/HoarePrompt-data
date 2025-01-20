(m, d) = map(int, input().split())
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_days = days_in_month[m - 1]
start_day = (d - 1) % 7 + 1
total_days = (month_days + start_day - 1) // 7
print(total_days + (1 if month_days % 7 != 0 else 0))