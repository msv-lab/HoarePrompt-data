a,b,c = map(int,raw_input().split())

f = False

if ((c% a == 0) or (c % b == 0)):
    print("Yes")
    f = True

else:
	i1 = 1
	i2 = 1
	while(a < c):
		a = a*i1
		while(b < c):
			b = b*i2
			d = a + b
			if(d == c):
				print("Yes")
				f = True
				break
			i2+=1
		i1+=1

if (f == False):
	print("No")

				
				

	   	  	    		 			 		 		 		 	