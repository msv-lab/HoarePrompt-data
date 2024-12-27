# coding: utf-8

winner = {1: 'Second', 2: 'First'}
n = int(raw_input())
array = list(map(int, raw_input().split()))
flag = 0

for x in array:
    if x & 1:
        print("First")
        flag = 1
        break

if flag == 0:
    print("Second")
