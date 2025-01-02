def chess(data):
   item = []
   for i in range(len(data)):
     if (data[i]!= '.'):
         item.append(data[i])
         
   p1 = 0
   p2 = 0
   q,Q = 9
   r,R=5
   b,B =3
   p,P=1
   dictb = {'q':9,'r':5,'b':3,'n':3,'p':1}
   dictw = {'Q':9,'R':5,'B':3,'N':3,'P':1}
   lb = [q,r,b,n,p]
   lw = [Q,R,B,N,P]
   
   for i in range(len(item)):
      for j in range(len(lb)):
         if (data[i] == lb[j]):
            p1 = p1 + dictb[lb[j]]
            
         if (data[i] == lw[j]):
            p1 = p1 + dictw[lw[j]]
            
   if (p1 < p2):
      return Black
   elif (p1 > p2):
      return White
   else:
      return Draw
         
            
	  	 	 				   		  	   	     			