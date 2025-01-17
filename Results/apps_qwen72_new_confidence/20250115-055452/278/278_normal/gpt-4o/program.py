n, a, b = map(int, input().split())

# Function to determine the round in which two teams will meet
def find_round(n, a, b):
    round_num = 0
    while n > 1:
        round_num += 1
        # Move to the next round
        a = (a + 1) // 2
        b = (b + 1) // 2
        # Check if they meet in this round
        if a == b:
            return round_num
        # Halve the number of teams for the next round
        n //= 2
    return round_num

# Calculate the round they meet
round_met = find_round(n, a, b)

# Print the result
if (1 << (round_met - 1)) == 2:
    print("Final!")
else:
    print(round_met)
