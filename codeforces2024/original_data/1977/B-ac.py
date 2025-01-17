for x in[*map(int,open(0))][1:]:
 r=[]
 while x:r+=x%2*(1-(x&2)),;x=x-r[-1]>>1
 print(len(r),*r)