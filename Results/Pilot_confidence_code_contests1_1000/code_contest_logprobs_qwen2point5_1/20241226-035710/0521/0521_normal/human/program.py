import math;
n=input();
i=0;
s=[];
if round(math.sqrt(n))==math.sqrt(n):
    while i<math.sqrt(n):
        i+=1;
        if n%i==0:
            res=(n/i)*(float((n+1-i)+1)/2);
            s.append(int(res));
            if i!=math.sqrt(n):
                res=i*(float((n+1-(n/i))+1)/2);
                s.append(int(res));                                    
else:
    while i<round(math.sqrt(n)):
        i+=1;
        if n%i==0:
            res=(n/i)*(float((n+1-i)+1)/2);
            s.append(int(res));
            res=i*(float((n+1-(n/i))+1)/2);
            s.append(int(res));        
s.sort();
print(s);