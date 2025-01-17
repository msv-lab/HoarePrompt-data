def solve():
    n = int(input()) # Number of vertices
    for _ in range(n):
        print('? {}'.format(n - 1))
        sys.stdout.flush()
        v, _ = map(int, input().split()) # Node with min degree and another node
        while True:
            print('? {}'.format(n - 2))
            sys.stdout.flush()
            v, u = map(int, input().split())
            if u == 0: break
        print('! {} '.format(v) + ' '.join(map(str, reversed(range(1, n+1)))))
        sys.stdout.flush()

if __name__ == "__main__":
    import sys
    from collections import defaultdict
    t = int(input()) # Number of testcases
    for _ in range(t):
        solve()