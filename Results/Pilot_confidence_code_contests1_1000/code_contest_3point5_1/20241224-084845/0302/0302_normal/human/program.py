n = int(raw_input())

def prime(n):
  for i in range(2, n):
    if n % i == 0:
      return i
  return n

cont = 0

if n%2 != 0:
  n -= prime(n)
  cont += 1

print (cont+n)/2
  	 						 									 			 	   	