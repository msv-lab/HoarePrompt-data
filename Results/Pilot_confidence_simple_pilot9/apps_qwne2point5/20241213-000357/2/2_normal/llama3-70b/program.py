x = int(input())

max_sum = 0
max_num = 0

for i in range(1, x + 1):
    digit_sum = sum(int(digit) for digit in str(i))
    if digit_sum > max_sum:
        max_sum = digit_sum
        max_num = i

print(max_num)
