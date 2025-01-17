# Read input
first_name, last_name = input().split()

# Initialize the earliest_login with a combination of the whole first name and one character of the last name
earliest_login = first_name + last_name[0]

# Iterate through each possible prefix of the first name
for i in range(1, len(first_name) + 1):
    # Iterate through each possible prefix of the last name
    for j in range(1, len(last_name) + 1):
        # Form the login by concatenating the prefixes
        login = first_name[:i] + last_name[:j]
        
        # Update the earliest_login if the current one is alphabetically earlier
        if login < earliest_login:
            earliest_login = login

# Print the result
print(earliest_login)
