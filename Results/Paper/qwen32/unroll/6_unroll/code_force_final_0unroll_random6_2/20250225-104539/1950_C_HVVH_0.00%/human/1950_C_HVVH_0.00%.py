day = 'AM'
n = int(input())
for _ in range(n):
    h,m = map(int, input().split(':'))
    if (h == 0):
        h = 12
        day = 'AM'
    elif h > 12:
        h = h - 12
        day = 'PM'
    else:
        day = 'PM'
        if h == 12:
            day = 'AM'
    print(f"{h:02d}:{m:02d}", day)