

# from math import factorial as fac
from collections import defaultdict
# from copy import deepcopy
import sys, math
f = None
try:
	f = open('q1.input', 'r')
except IOError:
	f = sys.stdin
if 'xrange' in dir(__builtins__):
	range = xrange
# print(f.readline())
# sys.setrecursionlimit(10**5)

	
def print_case_iterable(case_num, iterable):
	print("Case #{}: {}".format(case_num," ".join(map(str,iterable))))

def print_case_number(case_num, iterable):
	print("Case #{}: {}".format(case_num,iterable))

def print_iterable(A):
	print (' '.join(A))

def read_int():
	return int(f.readline().strip())
def read_int_array():
	return [int(x) for x in f.readline().strip().split(" ")]
def rns():
	a =  [x for x in f.readline().split(" ")]
	return int(a[0]), a[1].strip()
def read_string():
	return list(f.readline().strip())
def bi(x):
	return bin(x)[2:]










from copy import deepcopy
def solution(s,n,p,m):
	s = [0] + s
	dp = [[0 for _ in range(26)] for _ in range(n+1)]
	p.sort()
	for i in range(1,n+1):
		for j in range(26):
			dp[i][j] = dp[i-1][j] + int(j == (ord(s[i])-ord('a')))
	#total m+1 tries
	res = [x for x in dp[n]]
	for i in range(m):
		x=p[i]
		for j in range(26):
			res[j]+=dp[x][j]
	return ' '.join(map(str,res))





def main():
	T = read_int()
	for i in range(T):
		n,m = read_int_array()
		s = read_string()
		p = read_int_array()
		x = solution(s,n,p,m)

		if 'xrange' not in dir(__builtins__):
			print(x)
		else:
			print >>output,str(x)# "Case #"+str(i+1)+':',
	if 'xrange' in dir(__builtins__):
		print(output.getvalue())
		output.close()

if 'xrange' in dir(__builtins__):
	import cStringIO
	output = cStringIO.StringIO()
#example usage:
#    for l in res:
#       print >>output, str(len(l)) + ' ' +  ' '.join(l)

if __name__ == '__main__':
	main()



'''stuff you should look for
	* int overflow, array bounds
	* special cases (n=1?)
	* do smth instead of nothing and stay organized
	* WRITE STUFF DOWN
	* BITS - THINK HOW TO MASK PROPERLY
	* PERMUTATIONS - PARITY AND CYCLES
	* Think simple, if it becomes over complicated, try to look at it from a different perspective.
	* Have fun!!!
	* TRY FIXING SOMETHING, and then maybe binary search around it.
	* Remember heaps. 
	* Remember how to add a value to a segment when using prefix sum.
		suppose you have an array[1,2,3,4,5] and you want to add 3 to array[1:4]. Then just 
		add 3 to A[1], and decrease 3 from A[4]. Let's look at what happens:
		original prefixsums is 					 [1,3,6,10,15]
		array -> [1,5,3,4,2] and prefix sums are [1,6,9,13,15] 
		As you see, exactly +3 in A[1:4]
		*** The previous method can help checking how many x,y you can choose to get s=x+y from two arrays.
'''
'''
binary search 
	while(r - l > 1) {
		ll mid = l + (r - l) / 2;
		solve(mid);
		ll sum = 0;
		for (int i = 0; i < n; i++)
			sum += b[i];
		if (sum <= k)
			r = mid;
		else
			l = mid;
	}
'''
