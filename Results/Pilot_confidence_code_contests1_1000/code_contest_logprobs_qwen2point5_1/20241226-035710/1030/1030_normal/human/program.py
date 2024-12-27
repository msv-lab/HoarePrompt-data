b = int(raw_input())
i = 1
count = 0

while i <= b**0.5:
  if b % i == 0:
    if i**2 == b:
      count += 1
    else:
      count += 2
  i += 1

print(count)
 	   			  			 	  		  						   	