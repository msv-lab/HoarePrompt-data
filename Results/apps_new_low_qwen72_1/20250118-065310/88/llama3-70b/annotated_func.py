#State of the program right berfore the function call: m is an integer representing the month (1 ≤ m ≤ 12), and d is an integer representing the weekday of the first date of the month (1 ≤ d ≤ 7), where 1 is Monday and 7 is Sunday.
def func():
    m, d = map(int, input().split())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_days = days_in_month[m - 1]

start_day = (d - 1) % 7 + 1

total_days = (month_days + start_day - 1) // 7

print(total_days + (1 if month_days % 7 != 0 else 0))
#Overall this is what the function does:The function reads two integers `m` and `d` from user input, where `m` represents the month (1 ≤ m ≤ 12) and `d` represents the weekday of the first day of the month (1 ≤ d ≤ 7). It calculates the number of weeks in the month plus one if the month does not end on a Sunday. The function prints this value and does not return any value. The final state of the program includes the printed number of weeks plus one if necessary, but the function does not modify the input variables or any other state outside its scope. Note that the function does not handle leap years, which could affect the calculation for February.

