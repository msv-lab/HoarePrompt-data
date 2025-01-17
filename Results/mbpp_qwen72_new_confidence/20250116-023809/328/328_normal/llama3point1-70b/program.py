def is_polite(n):
    def count_divisors(num):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        return count

    num = 1
    while True:
        if count_divisors(num) == n:
            return num
        num += 1
