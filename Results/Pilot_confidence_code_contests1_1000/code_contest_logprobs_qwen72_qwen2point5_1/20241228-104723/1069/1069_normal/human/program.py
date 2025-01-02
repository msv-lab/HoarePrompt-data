from math import sqrt
for i in xrange(input()):
    a,b=map(int,raw_input().split())
    div1=(b/a)+1
    print (div1*div1*(b%a))+((div1-1)*(div1-1)*(a-(b%a)))
    
