def count_years_with_one_zero(a, b):
    def count_zeros(n):
        return bin(n).count('0')

    count = 0
    for year in range(a, b + 1):
        if count_zeros(year) == 1:
            count += 1
    return count

a, b = map(int, input().split())
print(count_years_with_one_zero(a, b))
