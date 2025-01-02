#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
input = sys.stdin
output = sys.stdout

MAX = 10**6

Da = 'Dasha'
Ma = 'Masha'

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    assert (a*b)/gcd(a,b) == (a/gcd(a,b))*b 
    #return (a*b)/gcd(a,b)
    return (a/gcd(a,b))*b

def GCD(numbers):
    return reduce(lambda a,b: gcd(a,b), numbers)

def LCM(numbers):
    return reduce(lambda a,b: lcm(a,b), numbers)


def f1(n):
    return n*(n+1)/2

def solve(a,b):
    G = gcd(a,b)
    L = lcm(a,b)
    if a<b:
        M = (L/b - 1)*G
        D = L - M
        if D>M:
            return Ma
        else:
            return Da
    else:
        M = (L/a - 1)*G
        D = L - M
        if D>M:
            return Ma
        else:
            return Da

S = input.readline().split(' ')
a = int(S[0])
b = int(S[1])
assert 1<=a and a<=MAX 
assert 1<=b and b<=MAX
assert a != b 

answer = solve(a,b)
    
output.write('%s\n' % (answer))
