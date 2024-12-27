import sys
input = sys.stdin.readline

def One(type):
	return (type(input()))
def List(type):
	return list(map(type,input().split()))
def Str():
	return (list(input()))
def Many(type):
	return map(type,input().split())


def main():
	n,c = One(int),List(int)
	g = {}
	for i in range(n): g[i]=[]

	for i in range(n-1):
		g[c[i]-1].append(i+1)

	cont = [0]*n
	vis = [False]*n

	for i in range(n-1,-1,-1):
		if len(g[i])==0:
			cont[i] = 1
		else:
			for nxt in g[i]:
				cont[i]+=cont[nxt]

	cont.sort()

	print(" ".join([str(cur) for cur in cont]))

main()
