def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def amicable_numbers_sum(limit):
    amicable_set = set()
    for num in range(2, limit + 1):
        if num not in amicable_set:
            sum_div = sum_of_divisors(num)
            if sum_div != num and sum_div <= limit:
                if sum_of_divisors(sum_div) == num:
                    amicable_set.add(num)
                    amicable_set.add(sum_div)
    return sum(amicable_set)

# Test cases
assert amicable_numbers_sum(999) == 504
assert amicable_numbers_sum(9999) == 31626
assert amicable_numbers_sum(99) == 0
