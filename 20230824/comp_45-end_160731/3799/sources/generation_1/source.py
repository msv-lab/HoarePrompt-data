s = input()

# Determine the length of the string
n = len(s)

# Check the first player, Takahashi, wins or not
if n % 2 == 0:
    # If the length of the string is even, Takahashi cannot remove any character
    # Therefore, Aoki wins
    print("Second")
else:
    # If the length of the string is odd, Takahashi can remove one character
    # Takahashi will remove a character in the middle of the string
    # This will make the length of the string even
    # Therefore, Takahashi wins
    print("First")