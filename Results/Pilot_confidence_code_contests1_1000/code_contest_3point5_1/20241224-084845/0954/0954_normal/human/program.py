from __future__ import division, print_function
import sys, math, bisect, itertools

input = lambda: sys.stdin.readline().rstrip()
def lii(): return list(map(int, input().split()))
def mii(): return map(int, input().split())

def solve():
    a = int(input())
    b = input(); c = input()
    first = 0; second = 0
    for i in range(a):
        if (int(b[i]) > int(c[i])):
            first += 1
        elif (int(b[i]) < int(c[i])):
            second += 1
    if (first > second): 
        print("RED")
    elif (second > first): 
        print("BLUE")
    else: 
        print("EQUAL")

def main():
    for _ in range(int(input())):
        solve()

if __name__ == '__main__':
  main()