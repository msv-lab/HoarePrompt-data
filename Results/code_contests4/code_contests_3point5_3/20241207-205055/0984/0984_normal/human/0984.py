import sys
import heapq
import bisect
import math
import random

INF = 10**9+7
OFFLINE = 0
sys.setrecursionlimit(INF)

def fi():
	return int(sys.stdin.readline())

def fi2():
	return map(int, sys.stdin.readline().split())

def fi3():
	return sys.stdin.readline().rstrip()

def fo(*args):
	for s in args:
		sys.stdout.write(str(s)+" ")
	sys.stdout.write("\n")
	#sys.stdout.flush()

def puts(*args):
	for s in args:
		sys.stdout.write(str(s));

##
if OFFLINE:
	sys.stdin = open("fin.txt", "r")
	sys.stdout = open("fout.txt", "w")
##



##main

n = fi()
a = fi2()

m = max(a)

cnt = 0

res = 0
for i in range(n):
	if a[i] == m:
		cnt += 1
	else:
		cnt = 0
	res = max(cnt, res)

fo(res)