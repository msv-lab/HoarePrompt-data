import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def solve(n, arr):
    sum = 0
    bitcount = [0]*100
    for num in arr:
        b = reversed(bin(num)[2:])
        for i, s in enumerate(b):
            if i != "0":
                bitcount[i] += int(s)
    for i, b in enumerate(bitcount):
        sum += b * (n-b) * 2**i
    return sum % (10**9 + 7)


def main():
    N = int(input())
    A_l = [int(i) for i in input().split()]
    print(solve(N, A_l))


if __name__ == "__main__":
    main()