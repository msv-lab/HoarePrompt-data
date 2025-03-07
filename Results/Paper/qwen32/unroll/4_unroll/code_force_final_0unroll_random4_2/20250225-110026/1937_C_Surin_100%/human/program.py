I = lambda : list(map(int, input().split(' ')))
R = lambda : (int(input()))
 
import sys
# import bisect
# from bisect import bisect_left, bisect_right
import math
 
for kp in range(int(input())):
 
    n = int(input())
    # sys.stdout.flush()
    # print()
 
    g = 0
    v1 = 0
    for i in range(1,n):
        # v1 = 0
        v2 = i
        print(f"? {v1} {v1} {v2} {v2}")
        sys.stdout.flush()
 
        r = input('')
        # print()
 
        if r == "<": v1 = v2
 
    prev = 0
    for i in range(1,n):
 
        print(f"? {v1} {i} {v1} {prev}")
        sys.stdout.flush()
        r = input()
 
        if r == '>': prev = i
 
        elif r == "=":
            print(f"? {i} {i} {prev} {prev}")
            sys.stdout.flush()
            r2 = input('')
 
            if r2 == '<': prev = i
 
    # print(prev,i)
    print(f"! {prev} {v1}")
    # print()
    sys.stdout.flush()