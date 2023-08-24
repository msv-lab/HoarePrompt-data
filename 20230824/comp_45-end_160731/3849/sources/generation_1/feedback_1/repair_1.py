def solve(n, k, cards):
    # If k is equal to 1, it is always a draw
    if k == 1:
        return "tokitsukaze"
    
    # If there are less than k cards, it is always a draw
    if n < k:
        return "once again"
    
    # If there are exactly k cards and they are all the same, it is a draw
    if n == k and cards.count(cards[0]) == n:
        return "once again"
    
    # If there are exactly k cards and they are not all the same, the second player wins
    if n == k and cards.count(cards[0]) != n:
        return "quailty"
    
    # If there are more than k cards and the first player can make a move that leaves a winning situation, they win
    for i in range(1, n-k+1):
        if cards[i-1] != cards[i+k-1]:
            return "tokitsukaze"
    
    # If there are more than k cards and the first player cannot make a move that leaves a winning situation, the second player wins
    return "quailty"

# Read input
n, k = map(int, input().split())
cards = input()

# Solve the problem
result = solve(n, k, cards)

# Print the result
print(result)