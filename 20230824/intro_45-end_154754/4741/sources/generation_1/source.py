
# Get the input as a string
temp = input()

# Split the input into numerator and denominator
numerator, denominator = map(int, temp.split('/'))

# Calculate the temperature in Celsius using the given formula
celsius_numerator = (numerator - 32) * 5
celsius_denominator = 9

# Find the greatest common divisor (gcd) of the numerator and denominator to reduce the fraction
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd_value = gcd(celsius_numerator, celsius_denominator)

# Reduce the fraction by dividing both numerator and denominator by the gcd
celsius_numerator //= gcd_value
celsius_denominator //= gcd_value

# Check if the temperature is negative and adjust the sign of the numerator accordingly
if celsius_numerator < 0:
    celsius_numerator *= -1
    sign = '-'
else:
    sign = ''

# Print the result in the required format
print(sign + str(celsius_numerator) + '/' + str(celsius_denominator))
