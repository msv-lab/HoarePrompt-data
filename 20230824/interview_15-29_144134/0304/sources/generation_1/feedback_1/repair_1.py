n = int(input())
length = len(str(n)) # length of the number
count = length - 1 # possible number of positions to swap

# check if all digits are the same
if len(set(str(n))) == 1:
    result = 1
elif length > 1:
    result = count * 2 + 1 # each position can have one of two digits, plus 1 for the original number
else:
    result = 1

print(result)