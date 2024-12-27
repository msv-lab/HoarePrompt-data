import sys
from itertools import permutations

def main():
	while True:
		n = input()
		k = input()
		if n == k == 0:
			sys.exit(0)
		for i in xrange(n):
			input()
#		nums = [raw_input().strip() for i in xrange(n)]
#		result = set(["".join(p) for p in permutations(nums, k)])
#		print (len(result))

if __name__ == '__main__':
	sys.exit(main())