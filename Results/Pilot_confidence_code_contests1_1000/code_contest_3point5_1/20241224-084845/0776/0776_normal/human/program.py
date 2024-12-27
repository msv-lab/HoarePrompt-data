from sys import stdin, stdout  

def main(): 
	n = stdin.readline() 
	arr = [int(x) for x in stdin.readline().split()] 
	dic = {1:6, 4:3, 2:5}
	for x in arr:
		res = 'NO'
		if x > 42:
			stdout.write(str(res)+'\n')
			continue
		if x < 22 :
			if x == 21 - 1:
				res = 'YES'
			elif x == 21 - 2:
				res = 'YES'
			if x == 21 - 3:
				res = 'YES'
			if x == 21 - 4:
				res = 'YES'
			if x == 21 - 5:
				res = 'YES'
			if x == 21 - 6:
				res = 'YES'
		if res == 'YES':
			stdout.write(str(res)+'\n')
			continue
		for i in dic:
			if x == 42 - (i + dic[i]) - 1:
				res = 'YES'
			elif x == 42 - (i + dic[i]) - 2:
				res = 'YES'
			elif x == 42 - (i + dic[i]) - 3:
				res = 'YES'
			elif x == 42 - (i + dic[i]) - 4:
				res = 'YES'
			elif x == 42 - (i + dic[i]) - 5:
				res = 'YES'
			elif x == 42 - (i + dic[i]) - 6:
				res = 'YES'
				res = 'YES'
		stdout.write(str(res)+'\n')
if __name__ == "__main__": 
	main()