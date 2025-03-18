def check_password(n, password):
    # Separate letters and digits
    letters = []
    digits = []
    
    # Split the password into letters and digits
    for ch in password:
        if ch.isdigit():
            digits.append(ch)
        else:
            letters.append(ch)
    
    # Check if letters are sorted in non-decreasing order
    if letters != sorted(letters):
        return "NO"
    
    # Check if digits are sorted in non-decreasing order
    if digits != sorted(digits):
        return "NO"
    
    # Check if there is any digit after a letter
    for i in range(len(password) - 1):
        if password[i].isalpha() and password[i + 1].isdigit():
            return "NO"
    
    return "YES"
 
# Input handling
t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())  # length of the password
    password = input().strip()  # password string
    print(check_password(n, password))