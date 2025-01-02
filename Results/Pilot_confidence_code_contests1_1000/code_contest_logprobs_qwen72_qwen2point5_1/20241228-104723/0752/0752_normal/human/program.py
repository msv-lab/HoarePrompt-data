
#import time
#the_start_time = time.time()
#import sys
#import random
#import os.path


def main():
	
	import sys
	#import math
	#from Queue import PriorityQueue
	
	
	_real_letters = ['A','H','I','M','O','T','U','V','W','X','Y']
	
	_name = sys.stdin.readline().strip()
	
	N = len(_name)
	_middle = N>>1 
	_decision = 'YES'
	if (_name[_middle] not in _real_letters):
		_decision = 'NO' 
	else:
		j = N-1
		for i in range(_middle):
			if (_name[i] !=  _name[j]):
				_decision = 'NO'
				break
			if (_name[i] not in _real_letters):
				_decision = 'NO'
				break
			j -= 1
		
		
	sys.stdout.write(str(_decision)+"\n")
	
	
if __name__ == "__main__":
	
	main()
	
	#elapsed_time = time.time() - the_start_time
	#print(elapsed_time)  