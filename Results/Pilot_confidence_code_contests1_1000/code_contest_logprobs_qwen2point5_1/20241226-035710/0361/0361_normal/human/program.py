def Time(mon,day,hour,min,sec):
    mons =[31,29,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(mon):
        days+=mons[i]
    return (days+day)*86400+3600*hour+60*min+sec
import sys
n,m = map(int,raw_input().split())
times = []
a = sys.stdin.readlines()
for i in range(len(a)):
    str1 = a[i]
    MM = int(str1[5:7])
    DD = int(str1[8:10])
    HH = int(str1[11:13])
    MIN = int(str1[14:16])
    SEC = int(str1[17:19])
    times.append(Time(MM,DD,HH,MIN,SEC))
for i in range(len(times)):
    tmp = 0
    j = i
    bol = False
    while j>=0 and times[i]-times[j]<n:
        j-=1
        tmp+=1
    if tmp>=m:
        print(a[i][:19])
        exit()
print(-1)


