import re

def validate_mobile_number(number):
    pattern = r'^[789]\d{9}$'
    if re.match(pattern, number):
        return "YES"
    else:
        return "NO"

# Read the number of inputs
n = int(input())

# Read and validate each number
for _ in range(n):
    number = input().strip()
    if number == "":
        print("NO")
    else:
        result = validate_mobile_number(number)
        print(result)