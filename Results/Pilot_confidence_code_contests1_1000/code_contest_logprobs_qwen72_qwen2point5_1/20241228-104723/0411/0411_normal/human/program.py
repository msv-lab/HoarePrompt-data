mod = 1000000007

raspuns = 1
v = []
n = 0

def factorial( n ):
    p = 1
    for i in range( 1, n + 1 ):
        p *= i
    #print( n, " -> ", p )
    return p

def combinari( n, k ):
    p = factorial( n ) / ( factorial( k ) * factorial( n - k ) )
    #print( n, k, " - > ", p )
    return p

k = input()
for i in range( k ):
    x = input()
    n += x
    v.append( x )

for i in v[::-1]:
    n -= 1
    i -= 1
    if i:
        raspuns *= combinari( n, i )
    n -= i

raspuns %= mod

print( raspuns )