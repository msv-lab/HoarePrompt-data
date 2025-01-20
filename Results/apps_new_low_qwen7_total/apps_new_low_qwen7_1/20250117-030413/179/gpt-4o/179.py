# Read the length of the string
n = int(input().strip())

# Read the string itself
s = input().strip()

# Determine the number of moves each player will make
moves = (n - 11) // 2

# Count the number of occurrences of '8' in the first (n - 11) characters
count_8 = s[:n-11].count('8')

# Vasya wins if there are more '8's than the number of non-'8' characters Petya can remove
if count_8 > moves:
    print("YES")
else:
    print("NO")
