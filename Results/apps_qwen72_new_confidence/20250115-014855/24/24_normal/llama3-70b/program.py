a = input()
b = input()

# Convert a to a list of digits
a_digits = [int(d) for d in a]

# Sort the digits in descending order
a_digits.sort(reverse=True)

# Construct the maximum possible number
max_num = int(''.join(map(str, a_digits)))

# If the maximum possible number exceeds b, try to find a smaller number
if max_num > int(b):
    for i in range(len(a_digits) - 1, -1, -1):
        if a_digits[i] < int(b)[0]:
            a_digits[i], a_digits[0] = a_digits[0], a_digits[i]
            break
    max_num = int(''.join(map(str, a_digits)))

print(max_num)
