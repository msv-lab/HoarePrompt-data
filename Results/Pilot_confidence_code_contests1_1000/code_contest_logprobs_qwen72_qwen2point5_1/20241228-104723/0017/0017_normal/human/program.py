def correct(m,d,y):
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if 0<m<13 and 0<d<=days[m-1] and 2013<=y<=2015:
        return True
    return False

s = [a for a in raw_input().split('-') if a!='']
yp = ['2014','2013','2015']
dates = dict()
for i in range(2,len(s)):
    if   s[i][:4] in yp:
        d,m,y = s[i-2][-2::1],s[i-1],s[i][:4]
        if len(d)!=2 or len(m)!=2 or len(y)!=4: continue;
        if correct(int(m),int(d),int(y)):
            dates[(d,m,y)]=dates.get((d,m,y),0)+1
ma = 0
mb = None
for a,b in dates.items():
    if b>ma:
        mb=a
        ma = b
print('-'.join(mb))
a=0