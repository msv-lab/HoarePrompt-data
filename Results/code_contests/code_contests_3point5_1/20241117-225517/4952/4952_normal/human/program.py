n=input()
s=list(raw_input())
ns=''

i=n-2
while(i>=0):
    ns+=s[i]
    i-=2

if n%2: i=0
else: i=1

while(i<n):
    ns+=s[i]
    i+=2

print(ns)
