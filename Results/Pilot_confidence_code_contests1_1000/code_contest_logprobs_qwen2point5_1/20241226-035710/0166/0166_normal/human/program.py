import sys
def fi():
    return int(sys.stdin.readline())

def fi2():
    return map(int, sys.stdin.readline().split())

def fi3():
    return sys.stdin.readline()

def fo(*args):
    for s in args:
        sys.stdout.write(str(s)+' ')
    sys.stdout.write('\n')

INF=10**9+7

#main

T=fi()
for t in range(T):
    n=fi()
    s=raw_input()
    if "<>" in s:
        fo(1)
    else:
        fo(0)
