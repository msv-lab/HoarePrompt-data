n = input()
length = len(n) # length of the number
count = length - 1 # possible number of positions to swap
result = count * 2 # each position can have one of two digits
if length > 1:
    result += 1 # add 1 for the original number
print(result)