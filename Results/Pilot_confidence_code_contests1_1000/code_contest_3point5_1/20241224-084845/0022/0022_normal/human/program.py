from __future__ import print_function
n=int(input())
l=[]
l[:n]=map(int,raw_input().split())

x=[]
y=[]
x[:n]=map(int,raw_input().split())
y[:n]=map(int,raw_input().split())
for i in l:
    if (x.count(i)==0):
        print(i)
        l.remove(i)
        break
for i in x:
    if (y.count(i)==0):
        print(i)
        break
