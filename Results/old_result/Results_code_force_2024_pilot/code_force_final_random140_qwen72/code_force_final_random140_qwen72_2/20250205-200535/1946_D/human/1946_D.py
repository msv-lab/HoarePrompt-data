def thing(arr, x):
 
	def find_new(cur_arr, bit):
		#if the current x bit is on then we have 2 options
		#1: turn it off (make all the ones with that bit even)
		#2: leave it on and continue
 
		#if the current x bit is off, we must 
 
		if bit == -1:
			return len(cur_arr)
 
		new_arr = []
		xor = 0
 
		for i in cur_arr:
			xor ^= i
			if not (xor >> bit) & 1:
				new_arr.append(xor)
				xor = 0
 
		if (xor >> bit) & 1:
			thing1 = -1
		else:
			thing1 = len(new_arr)
 
		if (x >> bit) & 1:
			return max(thing1, find_new(cur_arr, bit - 1))
		elif thing1 != -1:
			return find_new(new_arr, bit - 1)
		return -1
 
	return find_new(arr, 30)
 
 
 
testcases = range(int(input()))
 
for case in testcases:
	n, k = [int(i) for i in input().split(" ")]
	arr = [int(i) for i in input().split(" ")]
	print(thing(arr, k))