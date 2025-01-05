for _ in xrange(input()):
    a = input()
    c = 0
    if (a%2!=0):
        a = a-9
        c = 1    
        
    print -1 if a in (1,2,3,5,7,11) else a/4+c    