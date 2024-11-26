#!/usr/bin/env python2

import sys

input = iter(sys.stdin.readlines()).next

def main():
   K = int(input())
   S = input().strip()
   if len(S) <= K:
      print(S)
   else:
      print(S[:K] + '...')

   return 0

if __name__ == '__main__':
   sys.setrecursionlimit(10000)
   main()
