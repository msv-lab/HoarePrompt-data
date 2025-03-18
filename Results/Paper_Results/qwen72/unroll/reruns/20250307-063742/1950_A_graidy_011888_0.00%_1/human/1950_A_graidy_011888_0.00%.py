from random import randint
 
i = 1
while i <= 1000:
    x = randint(1, 9)
    y = randint(1, 9)
    z = randint(1, 9)
    res = ""
    
    if x < y:
        if y > z:
            res = "peak"
        elif y < z:
            res = "stair"
        else:
            res = "none"
    else:
        res = "none"
        
    print(x, y, z, sep=" ")
    print(res)
    
    i += 1