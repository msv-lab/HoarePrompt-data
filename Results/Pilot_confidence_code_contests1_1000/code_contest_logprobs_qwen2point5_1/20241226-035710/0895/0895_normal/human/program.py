import datetime as D
while 1:
  a,b,c,d,e,f=map(int,raw_input().split())
  try: print (D.date(d,e,f)-D.date(a,b,c)).days
  except: break