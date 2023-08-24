# Since we are looking for Pythagorean triples modulo n, we can use a nested loop to iterate through all possible values of a and b between 1 and n-1.
# For each pair (a, b), we will calculate c modulo n using the formula c = sqrt(a^2 + b^2).
# If the modulo of c with n is 0 (i.e., c is a multiple of n), then we have found a Pythagorean triple modulo n.
# We will count the number of Pythagorean triples modulo n and print the result.

import math

n = int(input())

count = 0

for a in range(1, n):
    for b in range(a, n):
        c = (a**2 + b**2)**0.5
        if c % n == 0:
            count += 1

print(count)