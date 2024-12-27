import os
import sys
import math

if __name__ == '__main__':
    count = int(sys.stdin.readline())
    while(count > 0):
        str_list = sys.stdin.readline().strip("\n").split(" ")
        number_list = [int(str(i)) for i in str_list]
        if(len(number_list)) < 5:
            break
        a = number_list[0]
        b = number_list[1]
        c = number_list[2]
        d = number_list[3]
        k = number_list[4]
        x =int(math.ceil(a / c))
        y = k - x
        if(y >= int(math.ceil(b / d))):
            print(str(x) + " " + str(y))
        else:
            print("-1")
        count = count - 1
	 	    			  		    	  						  		