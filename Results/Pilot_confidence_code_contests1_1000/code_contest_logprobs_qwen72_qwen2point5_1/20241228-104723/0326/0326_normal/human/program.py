from __future__ import print_function
import io
import sys
import math

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")

target = int(f.readline().strip())
target_str = str(target)

nums = []
X = target

num_bin = 2 ** len(target_str) - 1
num = int(str.format('{:b}', num_bin))

while num_bin > 0:
    while num <= X:
        nums.append(num)
        X -= num
    num_bin -= 1
    num = int(str.format('{:b}', num_bin))

print(len(nums))
print(str.join(' ', map(str, nums)))
