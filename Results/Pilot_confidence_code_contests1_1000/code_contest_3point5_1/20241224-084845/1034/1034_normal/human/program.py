from sys import stdin, stdout  
  
def main(): 
	n = stdin.readline() 
	res = ''
	for x in range(int(n)):
		a , b, n, S = [int(x) for x in stdin.readline().split()] 
		prod = n*a
		#if prod == S or b == S:
		#	res += 'YES \n'
		if n*a < S:
			if S - prod <= b:
				res += 'YES\n'
			else:			
				res += 'NO\n'
		else:
			if S % n <= b:
				res += 'YES\n'
			else:
				res += 'NO\n'
	stdout.write(res)
if __name__ == "__main__": 
	main()