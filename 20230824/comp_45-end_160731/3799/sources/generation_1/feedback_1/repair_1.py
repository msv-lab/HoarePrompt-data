s = input()

# Check the first player, Takahashi, wins or not
if s[0] != s[-1]:
    # If the first character and the last character are different, Takahashi wins
    print("First")
else:
    # If the first character and the last character are the same, Aoki wins
    print("Second")