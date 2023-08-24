# Get the input as a string
temp = input().strip()

# Remove the extra newline character if present
if temp[-1] == '\n':
    temp = temp[:-1]

# Split the input into numerator and denominator
numerator, denominator = map(int, temp.split('/'))

# Calculate the temperature in Celsius using the corrected formula
celsius_numerator = (numerator - 32) * 5
celsius_denominator = denominator * 9

# Find the greatest common divisor (gcd) of the numerator and denominator to reduce the fraction
def gcd(a, b):
    while a:
        a, b = b % a, a
    return b

gcd_value = gcd(celsius_numerator, celsius_denominator)

# Reduce the fraction by dividing both numerator and denominator by the gcd
celsius_numerator //= gcd_value
celsius_denominator //= gcd_value

# Check if the temperature is negative and adjust the sign of both numerator and denominator accordingly
if celsius_numerator < 0:
    celsius_numerator *= -1
    celsius_denominator *= -1

# Print the result in the required format
print(str(celsius_numerator) + '/' + str(celsius_denominator))