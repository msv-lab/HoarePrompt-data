import sys


def FairNut(peoples):
	mini=10**10
	for x in xrange(len(peoples)):
		unit_pp=0
		for i in xrange(len(peoples)):
			unit_pp+=(abs(i-x)+i+x)*peoples[i]
		mini=min(unit_pp,mini)
	return(mini)

n=int(raw_input())
l=map(int,raw_input().split())
print(FairNut(l)*2)
