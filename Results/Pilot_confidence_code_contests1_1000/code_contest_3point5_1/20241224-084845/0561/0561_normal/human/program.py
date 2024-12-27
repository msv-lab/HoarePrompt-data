a=[]
for i in range(5):
    a.append(int(input()))
b=set(map(lambda x: x%10,a))
if 0 in b:
    b.remove(0)
print(sum(map(lambda x:(x/10+1)*10 if x%10 != 0 else (x/10)*10,a))+min(b)-10)