# Read the input parentheses sequence
s = input()
 
# Initialize the prefix balance and store the necessary details
balance = 0
details = []
 
# Calculate prefix balance for each character in the sequence
for i, char in enumerate(s):
    if char == '(':
        balance += 1
    else:
        balance -= 1
    # Store the (balance, -position, character)
    # We use -position to automatically sort by decreasing position when balances are the same
    details.append((balance, -i, char))
 
# Sort by (balance, -position)
details.sort()
 
# Extract the characters from the sorted details
result = ''.join(char for _, _, char in details)
 
# Print the result
print(result)