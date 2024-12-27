import sys
import math
stringAW =  raw_input()
n,w = stringAW.split()
n = int(n)
w = int(w)

stringA = raw_input()
a = list(stringA.split())
a = map(int, a)

#list of tuples (how much filled, how much original, original place in string)
tlist = [[] for _ in range(n)]

for i in range(n):
    tlist[i] = [0, a[i], i]
tlist.sort(key=lambda tup : tup[1])

for i in range(n):
    tlist[i][0] += math.ceil(tlist[i][1]/2)
    w -= math.ceil(tlist[i][1]/2)

#If we are not able to fill all cups at least halfway, then we have failed
if(w < 0): 
    print(-1)
    sys.exit()


#While we still have water in our pot
inch = 0
while( w > 0 and inch < n):
    if(w >= tlist[inch][1] - tlist[inch][0]):
        w -= tlist[inch][1] - tlist[inch][0]
        tlist[inch][0] += tlist[inch][1] 
    else:
        tlist[inch][0] += w
        w = 0
    inch+= 1
tlist.sort(key=lambda  tup:tup[2], reverse=True)

if(inch == n):
    print(-1)
    sys.exit()

for i in range(n-1):
    sys.stdout.write("" + str(int(tlist[i][0])) + " ")

sys.stdout.write(str(int(tlist[n-1][0])))
sys.stdout.flush()



