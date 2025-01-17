import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def reverse_card():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        count = 0
        for b in range(1, min(n, m)+1):
            if b * gcd(a:=n, b) % (a + b) == 0:
                count += 1
        print(count)

reverse_card()