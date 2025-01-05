def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def choose(n, k):
    if k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    if k > n or k > m:
        print(0)
    else:
        res = (choose(n + m, k) - choose(n + m, k - 1))
        print(res)
 	 	 		   	  				  	   		  	 	