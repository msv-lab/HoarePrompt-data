k = int(input())

prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
powers = [0] * 10

index = 0
while k > 1 and index < 10:
    if k % prime_factors[index] == 0:
        powers[index] += 1
        k //= prime_factors[index]
    else:
        index += 1

# Construct the string
result = ''
for i in range(10):
    result += 'codeforces' * powers[i]

print(result)