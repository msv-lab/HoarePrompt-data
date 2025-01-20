def func_1(n):
    divisors_sum = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i != n:
                divisors_sum += i + n // i
            else:
                divisors_sum += i
    return divisors_sum - n

def func_2(n):
    amicable_sum = 0
    for num in range(1, n + 1):
        if func_1(num) < n:
            if func_1(func_1(num)) == num and num != func_1(num):
                amicable_sum += num
    return amicable_sum