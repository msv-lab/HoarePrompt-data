n = int(raw_input())
numbers = map(int, raw_input().split())
neg = 0
num_zeros = 0
needed_coins = 0
for num in numbers:
    if num < 0:
        neg += 1
    if num == 0:
        num_zeros += 1
    else:
        needed_coins += abs(num) - 1
if neg % 2 != 0:
    if num_zeros > 0:
        needed_coins += num_zeros
    else:
        needed_coins += 2
else:
    needed_coins += num_zeros
print(needed_coins)