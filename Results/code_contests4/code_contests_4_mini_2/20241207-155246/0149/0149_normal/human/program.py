import sys

n = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split(' ')))
p = [pi - 1 for pi in p]

even = odd = 0
for i in range(n/2):
	even += abs(i*2 - p[i]) 
	odd += abs(i*2+1 - p[i])

print(min(even,odd))