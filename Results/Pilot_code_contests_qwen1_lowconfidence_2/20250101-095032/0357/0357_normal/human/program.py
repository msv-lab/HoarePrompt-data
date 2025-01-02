import sys
testing = len(sys.argv) == 4 and sys.argv[3] == "myTest"
if testing:
    cmd = sys.stdout
    from time import time
    start_time = int(round(time() * 1000)) 
    input = open(sys.argv[1], 'r').readline
    readAll = open(sys.argv[1], 'r').read
    sys.stdout = open(sys.argv[2], 'w')
else:
    input = sys.stdin.readline
    readAll = sys.stdin.read

# ############ ---- I/O Functions ---- ############

# class InputData:
#     def __init__(self):
#         self.lines = readAll().split('\n')
#         self.n = len(self.lines)
#         self.ii = -1
#     def input(self):
#         self.ii += 1
#         assert self.ii < self.n
#         return self.lines[self.ii]
# inputData = InputData()
# input = inputData.input

def intin():
    return(int(input()))
def intlin():
    return(list(map(int,input().split())))
def chrin():
    s = input()
    return(list(s[:len(s) - 1]))
def strin():
    s = input()
    return s[:len(s) - 1]
def intlout(l, sep=" "):
    print(sep.join(map(str, l)))
    
# ############ ---- I/O Functions ---- ############

# from math import ceil
# from collections import defaultdict as dd
# from heapq import *
# from Queue import Queue

def getDiv(n):
    i = 1
    sq_n = n**0.5
    divs = []
    while i <= sq_n:
        if n%i==0:
            divs.append(i)
            if n / i != i:
                divs.append(n/i)
        i = i + 1
    return sorted(divs)     # unsorted

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2)==0:
            return False
        i += 6
    return True

def BS(arr, x, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid, mid
        elif arr[mid] > x:
            return BS(arr, x, low, mid - 1)
        else:
            return BS(arr, x, mid + 1, high)
    else:
        return high, low

p = [False]*21001
for i in xrange(1,21001):
    p[i] = isPrime(i)
primes = [i for i,x in enumerate(p) if x]
# print(primes)
def main():
    d = intin()
    i = BS(primes, d+1, 0, len(primes)-1)[1]
    j = i+1
    while primes[j] - primes[i] < d:
        j += 1
    print(primes[i]*primes[j])
    


if __name__ == "__main__":
    for _ in xrange(intin()):
        main()
    # for i in xrange(1,11001):
    #     a = getDiv(i)
    #     if len(a) >= 4:
    #         print(i, a)
        # print("YES" if main() else "NO")
    # main()

    if testing:
        sys.stdout = cmd
        print(int(round(time() * 1000))  - start_time)