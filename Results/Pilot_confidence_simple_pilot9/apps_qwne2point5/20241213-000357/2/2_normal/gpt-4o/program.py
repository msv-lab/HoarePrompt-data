def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

x = int(input().strip())

# Convert x to a string to manipulate digits
x_str = str(x)
n = len(x_str)

# Generate a candidate number by replacing the last non-zero digit with zero and all following digits with 9
if x_str[0] != '1':
    candidate = int(x_str[0]) - 1
    candidate = str(candidate) + '9' * (n - 1)
else:
    candidate = '9' * (n - 1)
candidate = int(candidate)

# Compare sum of digits of x and candidate
sum_x = sum_of_digits(x)
sum_candidate = sum_of_digits(candidate)

if sum_candidate > sum_x:
    print(candidate)
else:
    print(x)
