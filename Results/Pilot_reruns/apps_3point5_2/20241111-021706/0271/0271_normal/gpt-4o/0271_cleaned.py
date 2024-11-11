n = int(input())
remainder = n % 10
if remainder <= 5:
    result = n - remainder
else:
    result = n + (10 - remainder)
print(result)