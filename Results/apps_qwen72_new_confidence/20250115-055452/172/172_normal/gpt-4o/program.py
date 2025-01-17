password = input()

def is_complex(password):
    if len(password) < 5:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    return has_upper and has_lower and has_digit

if is_complex(password):
    print("Correct")
else:
    print("Too weak")
