a=map(int,raw_input().split(":"))
c=a[0]*60+a[1]
a=map(int,raw_input().split(":"))
c+=a[0]*60+a[1]
c/=2
d=map(str,divmod(c,60))
if len(d[0])==1:
	d[0]="0"+d[0]
if len(d[1])==1:
	d[1]="0"+d[1]
