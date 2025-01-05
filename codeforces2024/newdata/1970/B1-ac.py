n=int (input ())
a=map (int,input ().split ())
a=list (a)
print ('YES')
for i in range (1,n+1):
    print (i,i)
for i in range (1,n+1):
    if i>a[i-1]/2:
        print (i-int (a[i-1]/2),end=' ')
    else:
        print (i+int (a[i-1]/2),end=' ')