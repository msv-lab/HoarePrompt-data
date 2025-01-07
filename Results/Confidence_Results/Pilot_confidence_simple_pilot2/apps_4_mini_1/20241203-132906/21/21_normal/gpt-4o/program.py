def is_palindrome(time):
    return time == time[::-1]

def add_minute(hh, mm):
    mm += 1
    if mm == 60:
        mm = 0
        hh += 1
        if hh == 24:
            hh = 0
    return hh, mm

def format_time(hh, mm):
    return f"{hh:02}:{mm:02}"

def min_minutes_to_palindrome(hh, mm):
    minutes = 0
    while True:
        time = format_time(hh, mm)
        if is_palindrome(time):
            return minutes
        hh, mm = add_minute(hh, mm)
        minutes += 1

if __name__ == "__main__":
    time = input().strip()
    hh, mm = map(int, time.split(':'))
    print(min_minutes_to_palindrome(hh, mm))
