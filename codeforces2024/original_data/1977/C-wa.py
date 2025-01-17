# import sys
# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

from math import gcd

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = 0
        a.sort()
        m = {}
        for it in a:
            m[it] = m.get(it, 0) + 1
        v = list(m.keys())
        for i in range(len(v)-1, -1, -1):
            cur = v[i]
            length = m[cur]
            f = 0
            for j in range(i-1, -1, -1):
                lc = cur * v[j] // gcd(cur, v[j])
                if lc > v[-1]:
                    f = 1
                    length = n
                    break
                if m.get(lc, 0) > 0 and lc != cur:
                    continue
                length += m.get(v[j], 0)
                cur = lc
                if cur not in m:
                    ans = max(ans, length)
            if f:
                ans = n
                break
            if length == 1:
                continue
            if m.get(cur, 0) > 0:
                continue
            ans = max(ans, length)
            if ans == n:
                break
        print(ans)

if __name__ == "__main__":
    main()