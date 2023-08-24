n = int(input())

# Initialize the minimum number of coins to be exchanged as 0
min_coins = 0

# Loop through each power of 10 starting from the largest
power = 1
while n > 0:
    # Calculate the number of coins of the current power of 10 that the customer can use
    coins = n % 10
    
    # If the number of coins is less than 5, no need to exchange
    if coins < 5:
        min_coins += coins
    # If the number of coins is equal to 5, exchange 5 coins for a coin of the next power of 10
    elif coins == 5:
        min_coins += 1
    # If the number of coins is greater than 5, exchange 10 - coins for a coin of the next power of 10
    else:
        min_coins += 10 - coins
    
    # Divide the payment by 10 to move to the next power of 10
    n //= 10
    
    # Increment the power of 10
    power *= 10

print(min_coins)