# import random
# import itertools
# from sys import stdin, stdout
# import operator
# import collections
import bisect
import collections
import heapq
import math
import sys
from sys import maxsize
# from decimal import Decimal
 
#sys.setrecursionlimit(10**6)
 
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.buffer.readline())
def MI(): return map(int, sys.stdin.buffer.readline().split())
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def BI(): return sys.stdin.buffer.readline().rstrip()
def SI(): return sys.stdin.buffer.readline().rstrip().decode()
def li(): return [int(i) for i in input().split()]
def lli(rows): return [li() for _ in range(rows)]
def si(): return input()
def ii(): return int(input())
def ins(): return input().split()
 
 
# mod = 998244353
# fval = [1]
# for i in range(1,1002):
#     x = (fval[-1]*i)%mod
#     fval.append(x)
# #
# ifac = [1]*(1002)
# ifac[1001] = pow(fval[1001], -1, mod)
# for i in range(1001-1, 1, -1): ifac[i] = ifac[i+1]*(i+1)%mod
# print(fval)
# print(ifac)
# _________________ For taking Input from the Text Files __________________
# import os.path
#
# if (os.path.exists('input.txt')):
#     sys.stdin = open("input.txt", "r")
#     sys.stdout = open("output.txt", "w")
#     sys.stderr = open("error.txt", "w")
 
def drank(d, processing, da, rank):
    tmp = 10 ** 9
    if len(d[da]) == 1:
        return 1
    for di in d[da]:
        if processing[di - 1] == 0:
            processing[di - 1] = 1
            tmp = min(tmp, drank(d, processing, di, rank))
            processing[di - 1] = 0
    rank[da - 1] = tmp + 1
    return tmp + 1
 
# def primeFactors(n, d):
#     if (n % 2 == 0):
#         d[2] = 0
#     while n % 2 == 0:
#         d[2] += 1
#         n = n // 2
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if (n % i == 0):
#             d[i] = 0
#         while n % i == 0:
#             d[i] += 1
#             n = n // i
#     if n > 2:
#         d[n] = 1
# def powerofadivisor(n,div):
#     x = 0
#     while n%div == 0:
#         n//=div
#         x+=1
#     return x
 
#import heapq as hq
#import math
 
def gcd(a,b):
    if b==0:
        x = 1
        y = 0
        return x, y, a
    x, y, g = gcd(b, a%b)
    return y, x- (a//b)*y, g
 
# mod = 998244353
#
# is_prime = [True]*(10**7+5)
# primes = []
# def primeseive(n):
#     is_prime[0] = is_prime[1] = False
#     for i in range(4,n+1,2): is_prime[i] = False
#     i = 3
#     while i*i<=n:
#         if is_prime[i] == True:
#             for j in range(i*i,n+1,i):
#                 is_prime[j] = False
#         i+=2
    # for i in range(n):
    #     if is_prime[i]: primes.append(i)
 
def check(a, n, m, k):
    for i in range(n):
        if a[i]<m:
            k-= (m - a[i])
    if k>=0: return 1
    return -1
 
def solve():
    n, m = li()
    i = 1
    ans = 0
    while i*i<=(n+i):
        ans+= (n+i)//(i*i)
        i+=1
    return ans-1
 
    # a = li()
    # mini = min(a)
    # maxi = max(a)
    # x = maxi - mini
    # if x==0: return 0
    # p = math.floor(math.log2(x))+1
    # ans = ''
    # while x!=1:
    #     d = (x+1)//2 + mini
    #     maxi =
    #     ans += str((x+1)//2+mini)
    #     maxi =
    # return str(p)+ '\n' + ans
 
 
def main():
    # primeseive(10**7+2)
    # print(is_prime)
    for _ in range(ii()):
        sys.stdout.write(str(solve()) + "\n")
        #solve()
        # si()
        #print("? {} {}".format(low, mid), flush=True)
        # print(solve(), flush=True)
    # print(solve())
 
    #     z += str(ans) + '\n'
    # print(len(ans), ' '.join(map(str, ans)), sep='\n')
    # stdout.write(z)
 
 
# for interactive problems
# print("? {} {}".format(l,m), flush=True)
# or print this after each print statement
# sys.stdout.flush()
 
 
if __name__ == "__main__":
    main()