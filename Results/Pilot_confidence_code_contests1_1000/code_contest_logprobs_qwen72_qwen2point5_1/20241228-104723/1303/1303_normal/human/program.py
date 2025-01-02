from sys import stdin
from itertools import repeat
import math

def main():
    n = input()
    a = []
    
    for i in range(n):
        k = raw_input().split(":")
        a.append(int(k[0]) * 60 + int(k[1]))
    
    max = 0
    a = sorted(a)
    
    deck = 1
    
    for i in range(n - 1):
        if a[i + 1] - a[i] - deck > max:
            if a[i + 1] - a[i] == 1:
                deck += 1
            else:
                deck = 1
            max = a[i + 1] - a[i] - deck
     
    if 1440 - a[n - 1]  + a[0] - deck > max:
        if 1440 - a[n - 1]  + a[0] == 1:
            deck += 1
        else:
            deck = 1
        max = 1440 - a[n - 1]  + a[0] - deck
        
    hours = int(math.ceil(max / 60))
    
    mins = max - hours * 60;
    
    hours_s = str(hours)
    mins_s = str(mins)
    
    if hours < 10:
        hours_s = "0" + hours_s
    if mins < 10:
        mins_s = "0" + mins_s
    
    print(hours_s + ":" + mins_s)
    
    
    
main()