import sys
testing = len(sys.argv) == 4 and sys.argv[3] == "myTest"
if testing:
    cmd = sys.stdout
    from time import time
    start_time = int(round(time() * 1000)) 
    input = open(sys.argv[1], 'r').readline
    sys.stdout = open(sys.argv[2], 'w')
else:
    input = sys.stdin.readline

from collections import defaultdict
############ ---- Input Functions ---- ############
def intin():
    return(int(input()))
def inltin():
    return(list(map(int,input().split())))
def chrltin():
    s = input()
    return(list(s[:len(s) - 1]))
def strin():
    s = input()
    return s[:len(s) - 1]
    
def main():
    n = intin()
    M = []
    k = 0
    for _ in xrange(n):
        M.append(chrltin())
        k += sum([1 for x in M[-1] if x in 'XO'])
    K = int(k/3.0)

    clr = dict()
    cnt = [0]*3
    for i in xrange(n):
        for j in xrange(n):
            if M[i][j] == 'X':
                clr[(i,j)] = (i+j)%3
                cnt[(i+j)%3] += 1
            else:
                clr[(i,j)] = -1
    use_clr = 0
    while use_clr < 3 and (cnt[use_clr] > K or cnt[use_clr] == 0):
        use_clr += 1
    
    chg = 0
    for i in xrange(n):
        for j in xrange(n):
            if clr[(i,j)] == use_clr:
                M[i][j] = 'O'
                chg += 1
    for i in xrange(n):
        print(''.join(M[i]))

if __name__ == "__main__":
    for _ in xrange(intin()):
        main()

    if testing:
        sys.stdout = cmd
        print(int(round(time() * 1000))  - start_time)