def is_strong_password(password):
    digits = []
    letters = []
 
    for char in password:
        if char.isdigit():
            digits.append(char)
        else:
            letters.append(char)
 
    # Check if no digit appears after any letter
    last_digit_index = -1
    for i, char in enumerate(password):
        if char.isdigit():
            last_digit_index = i
        elif last_digit_index != -1:
            return "NO"
 
    # Check if digits are sorted in non-decreasing order
    if digits != sorted(digits):
        return "NO"
 
    # Check if letters are sorted in non-decreasing order
    if letters != sorted(letters):
        return "NO"
 
    return "YES"
 
# Read input
import sys
input = sys.stdin.read
data = input().split()
 
t = int(data[0])
index = 1
results = []
 
for _ in range(t):
    n = int(data[index])
    password = data[index + 1]
    index += 2
    results.append(is_strong_password(password))
 
# Output results
print("\n".join(results))