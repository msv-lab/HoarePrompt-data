def determine_winner(a, b):
    # If the sum of coins is odd, Alice wins, because she can always force Bob
    # to face an empty wallet scenario first due to having the first move advantage.
    # For an even sum, Bob wins, by following Alice's strategy and ensuring
    # that Alice faces the empty wallet scenario first.
    if (a + b) % 2 == 0:
        return "Bob"
    else:
        return "Alice"
 
def main():
    t = int(input("Enter the number of test cases: "))  # Read the number of test cases
    
    results = []
    
    for _ in range(t):
        a, b = map(int, input().strip().split())  # Read the number of coins in Alice's and Bob's wallets
        winner = determine_winner(a, b)
        results.append(winner)
    
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()