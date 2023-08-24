
n = int(input())

# Create a dictionary to map each digit to the required number of broken sticks
digit_map = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

# Initialize the count of good integers to 0
count = 0

# Check if the input is single digit
if n < 10:
    # Handle single digit input
    required_sticks = digit_map[str(n)]
    if required_sticks <= 2:
        count += 1
else:
    # Split the input number into its two digits
    digit1 = n // 10
    digit2 = n % 10

    # Calculate the required number of broken sticks for each digit
    required_sticks = digit_map[str(digit1)] + digit_map[str(digit2)]

    # Calculate the count of 0's and 9's in the input number
    count_zeros = str(n).count('0')
    count_nines = str(n).count('9')

    # Check if the sum of the counts is greater than or equal to the required number of broken sticks
    if count_zeros + count_nines >= required_sticks:
        count += 1

# Print the count of good integers
print(count)
  