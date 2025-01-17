def move_num(s: str) -> str:
    # Lists to hold alphabetic and numeric characters separately
    alpha_part = []
    num_part = []
    
    # Traverse each character in the string
    for char in s:
        if char.isdigit():
            num_part.append(char)
        else:
            alpha_part.append(char)
    
    # Join the alphabetic characters and numeric characters into a single string
    result = ''.join(alpha_part) + ''.join(num_part)
    
    return result

# Test cases
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'
