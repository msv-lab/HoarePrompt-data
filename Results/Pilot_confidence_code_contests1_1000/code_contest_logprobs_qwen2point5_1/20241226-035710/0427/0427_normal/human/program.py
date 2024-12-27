import itertools
import math
n = input()

chars = ["3", "5", "7"]
ndigits = int(math.log10(n)) + 1

count = 0
for digit in range(3, ndigits + 1):
    for string in itertools.product(chars, repeat=digit):
        if(string.count("3") == 0):
            continue
        if(string.count("5") == 0):
            continue
        if(string.count("7") == 0):
            continue
        if n >= int("".join(string)):
            count += 1

print(count)
