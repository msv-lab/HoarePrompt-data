n = int(input())

min_coins = 0
power = 1

while n > 0:
    coins = n // 10  # Fix for Bug 1

    if coins < 5:  # Fix for Bug 2
        min_coins += coins
    elif coins == 5:  # Fix for Bug 3
        min_coins += 1
    else:
        min_coins += coins - 5  # Fix for Bug 4
        min_coins += coins % 5  # Fix for Bug 4

    n //= 10
    power *= 10  # Fix for Bug 5

print(min_coins)