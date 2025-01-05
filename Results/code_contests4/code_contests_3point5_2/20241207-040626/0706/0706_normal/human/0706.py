from sys import stdin,stdout,setrecursionlimit,maxint,exit
setrecursionlimit(2*10**5)
#from os.path import dirname
#currdir=dirname(__file__)
#stdin=open(currdir+"/inputfile","r")
#stdout=open(currdir+"/output1.txt","w")
def listInput():
 return map(long,stdin.readline().split())
def printBS(li):
 if not li: return
 for i in xrange(len(li)-1):
  stdout.write("%d "%li[i])
 stdout.write("%d\n"%li[-1])
def sin():
 return stdin.readline().rstrip()
n=int(sin())
li=listInput()
N=max(li)
done=[0]*(N+1)
nos=[0]*(N+1)
primCount=[0]*(N+1)
for i in li:
 nos[i]+=1
for i in xrange(2,N+1):
  if done[i]==0:
   for j in xrange(i,N+1,i):
    done[j]=1
    if nos[j]: primCount[i]+=nos[j]
for i in xrange(1,N+1):
 primCount[i]+=primCount[i-1]
m=int(sin())
#print primCount
for i in xrange(m):
 l,r=listInput()
 if r>N: r=N
 if l>N: l=N+1
 stdout.write("%d\n"%(primCount[r]-primCount[l-1]))
