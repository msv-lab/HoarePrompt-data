def is_strong_password(t, test_cases):
    results = []
    
    for n, password in test_cases:
        # Split letters and digits
        letters = ""
        digits = ""
        for ch in password:
            if ch.isalpha():
                letters += ch
            elif ch.isdigit():
                digits += ch
        
        # Check if letters and digits are both sorted in non-decreasing order
        if list(letters) != sorted(letters) or list(digits) != sorted(digits):
            results.append("NO")
            continue
        
        # Check if letters appear before digits
        if letters and digits and password.index(letters[-1]) > password.index(digits[0]):
            results.append("NO")
        else:
            results.append("YES")
    
    return results
 
 
# Input Reading
t = int(input("Number of test cases, t = "))  # Number of test cases
test_cases = []
for _ in range(t):
    n = int(input("Length of password, n: "))  # Length of the password (we won't actually use this value)
    password = input("enter passowrd: ").strip()
    test_cases.append((n, password))
 
# Get the result
results = is_strong_password(t, test_cases)
 
# Output the results
for result in results:
    print(result)