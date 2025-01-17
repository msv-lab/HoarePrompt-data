n = int(input())
while True:
    n += 1
    str_n = str(n)
    count_non_zero = sum(1 for digit in str_n if digit != '0')
    if count_non_zero <= 1:
        print(n - int(input()))
        break
