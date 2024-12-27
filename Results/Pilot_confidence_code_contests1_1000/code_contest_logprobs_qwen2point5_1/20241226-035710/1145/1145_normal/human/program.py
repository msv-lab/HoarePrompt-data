f = open("data.txt", 'r')
file = f.read()
f.close()
lines = file.split("\n")
r = lines[1].split(" ")

serach_flag = True
old_mid = -1
min = 0
max = 10**9
mid = 0

low = -1
high = -1

while(serach_flag):
    mid = (min + max) / 2
    val = mid
    for k in r:
        val = val - (val % int(k))
    
    #print(min, mid, max, val)    
    if(val == 2):
        serach_flag = False
        break
        
    if(abs(mid - old_mid) < 1):
        break
    
    if(val == 0):    
        min = mid
    else:    
        max = mid

    old_mid = mid
    
#print(mid, serach_flag)


if(serach_flag == False):
    old_mid = -1
    low = mid
    high = mid

    minl = min
    maxl = mid
    midl = 0

    serach_flag = True  
    while(serach_flag):
        midl = (minl + maxl) / 2
        val = midl
        for k in r:
            val = val - (val % int(k))
        
        #print(minl, midl, maxl, val)
            
        if(abs(midl - old_mid) < 1):
            serach_flag = False
        
        if(val == 2):    
            maxl = midl
            low = midl
        else:
            minl = midl
        
        old_mid = midl
    #print(low, serach_flag)

    old_mid = -1
    minh = mid
    maxh = max
    midh = 0

    serach_flag = True   
    while(serach_flag):
        midh = (minh + maxh) / 2
        val = midh
        for k in r:
            val = val - (val % int(k))
        
        #print(minh, midh, maxh, val)

        if(abs(midh - old_mid) < 1):
            serach_flag = False
            
        if(val == 2):    
            minh = midh
            high = midh
        else:    
            maxh = midh
        
        old_mid = midh

    #print(high, serach_flag)    
    print(low, high) 
    
else:
    print(-1)

    
    