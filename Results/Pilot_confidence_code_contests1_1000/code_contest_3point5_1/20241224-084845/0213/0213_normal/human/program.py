
n, L, a = map(int, raw_input().split())
ltime = 0
allb = 0
for i in range(n):
    ti, li = map(int, raw_input().split())
    btime = ti - ltime
    if btime > a:
        allb = allb + (btime // a)
    ltime = ti + li
if L > ltime:
    btime = L - ltime
    allb = allb + (btime // a)
print(allb)

  		  			       					    		  	