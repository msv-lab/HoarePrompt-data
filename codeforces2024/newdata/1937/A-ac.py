import sys
input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    print(1<<(len(bin(N)[2:])-1))