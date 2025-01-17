def min_replacements_to_lucky_ticket(ticket):
    # Split the ticket into two halves
    first_half = ticket[:3]
    second_half = ticket[3:]
    
    # Calculate the sum of digits in both halves
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)
    
    # If the sums are already equal, no replacements are needed
    if sum_first_half == sum_second_half:
        return 0
    
    # Calculate the difference between the two sums
    diff = abs(sum_first_half - sum_second_half)
    
    # Create lists of digits from both halves
    first_half_digits = [int(digit) for digit in first_half]
    second_half_digits = [int(digit) for digit in second_half]
    
    # Create a list of all possible changes to reduce the difference
    changes = []
    
    for digit in first_half_digits:
        changes.append(9 - digit)  # max change for a digit in first half
        
    for digit in second_half_digits:
        changes.append(digit)  # max change for a digit in second half
    
    # Sort the changes in descending order to use the largest changes first
    changes.sort(reverse=True)
    
    # Try to reduce the difference using the largest possible changes
    replacements = 0
    for change in changes:
        diff -= change
        replacements += 1
        if diff <= 0:
            return replacements
    
    return replacements

# Read input
ticket = input().strip()

# Print the result
print(min_replacements_to_lucky_ticket(ticket))
