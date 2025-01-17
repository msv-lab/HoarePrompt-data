def determine_winner(n, piles):
    # Check if all piles have the same number of stones
    if all(pile == piles[0] for pile in piles):
        # If all piles are the same, Alice will always lose because Bob can mirror Alice's moves
        return "Bob"
    else:
        # If not all piles are the same, Alice can always find a way to guarantee a win
        return "Alice"

# Read input
n = int(input())
piles = list(map(int, input().split()))

# Determine and print the winner
print(determine_winner(n, piles))
