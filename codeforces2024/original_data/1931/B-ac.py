for s in[*open(0)][2::2]:
 a=*map(int,s.split()),;u=sum(a)//len(a);d=f=0
 for x in a:d+=x-u;f|=d
 print('YNEOS'[f<0::2])