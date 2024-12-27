import sys
from scipy.sparse import*
f=lambda*z:map(int,sys.stdin.readline().split())
n,=f();a,b,c=zip(*map(f,xrange(~-n)));q,k=f();r=[0]*q
z=map(int,csgraph.dijkstra(csr_matrix((c,(a,b)),[n+1]*2),0,k)[1:])
for _ in range(q):x,y=f();r[_]=str(z[x-1]+z[y-1])
sys.stdout.write('\n'.join(r))