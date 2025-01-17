s = input()
has_upper = any(c.isupper() for c in s)
has_lower = any(c.islower() for c in s)
has_digit = any(c.isdigit() for c in s)
if len(s) >= 5 and has_upper and has_lower and has_digit:
    print("Correct")
else:
    print("Too weak")
