k = int(input())

prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
powers = [0] * 25

index = 0
while k > 1 and index < 25:
    if k % prime_factors[index] == 0:
        powers[index] += 1
        k //= prime_factors[index]
    else:
        index += 1

# Construct the string
result = ''
for i in range(25):
    result += 'codeforces' * powers[i]

print(result)