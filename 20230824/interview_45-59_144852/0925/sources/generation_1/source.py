n = input()

# Create a dictionary to map each digit to the required number of broken sticks
digit_map = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

# Initialize the count of good integers to 0
count = 0

# Iterate over all possible integers from 0 to 99
for i in range(100):
  # Split the integer into its two digits
  digit1 = str(i // 10)
  digit2 = str(i % 10)
  
  # Calculate the required number of broken sticks for each digit
  required_sticks = digit_map[digit1] + digit_map[digit2]
  
  # Check if the required number of broken sticks matches the actual number
  if required_sticks <= n.count('0'):
    count += 1

# Print the count of good integers
print(count)