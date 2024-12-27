s=raw_input()
ln=len(s)
if ln%2==1:
	print -1
else:
	ll,rr,uu,dd=0,0,0,0
	for ch in s:
		if ch=='L':
			ll+=1
		elif ch=='R':
			rr+=1
		elif ch=='U':
			uu+=1
		elif ch=='D':
			dd+=1
	print (max((max(ll,rr)-min(ll,rr)),(max(dd,uu)-min(dd,uu)))+1)/2

