from __future__ import print_function

def try_hop(field, i):
	for slice_len in xrange(1, len(field)+1):
		res = field[i::slice_len]
		#print(i, slice_len, res)
		if len(res) == 5 and set(res) == {'*'}:
			return slice_len
	return 0

def main():
	n = int(raw_input())
	field = raw_input()
	win = False
	for i in xrange(n):
		if field[i] != '.':
			slice_len = try_hop(field, i)
			if slice_len:
				j = i+4*slice_len
				#print(j)
				if j+slice_len >= n or field[j+slice_len] == '*':
					win = True
					break
	if win:
		print('yes')
	else:
		print('no')

if __name__ == '__main__':
	main()

