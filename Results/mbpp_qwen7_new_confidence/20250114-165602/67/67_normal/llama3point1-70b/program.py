def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i != n:
                divisors_sum += i + n // i
            else:
                divisors_sum += i
    return divisors_sum - n

def amicable_numbers_sum(n):
    amicable_sum = 0
    for num in range(1, n + 1):
        if sum_of_divisors(num) < n:
            if sum_of_divisors(sum_of_divisors(num)) == num and num != sum_of_divisors(num):
                amicable_sum += num
    return amicable_sum
