n = int(input())

def is_lucky(year):
    digits = list(str(year))
    count_non_zero = sum(1 for d in digits if d != '0')
    return count_non_zero <= 1

next_year = n + 1
while not is_lucky(next_year):
    next_year += 1

print(next_year - n)
