def manacher(n, s):
    if n == 0:
        return []
    res = [0] * (2 * n - 1)
    l, r = -1, -1
    for z in range(2 * n - 1):
        i = (z + 1) // 2
        j = z // 2
        p = 0 if i >= r else min(r - i, res[2 * (l + r) - z])
        while j + p + 1 < n and i - p - 1 >= 0:
            if s[j + p + 1] != s[i - p - 1]:
                break
            p += 1
        if j + p > r:
            l = i - p
            r = j + p
        res[z] = p
    return res

def main():
    tt = int(input())
    for _ in range(tt):
        n, q = map(int, input().split())
        s = input().strip()
        p1 = [0] * (n + 2)
        p2 = [0] * (n + 2)
        for i in range(n + 1, -1, -1):
            if i >= n:
                p1[i] = p2[i] = i
            else:
                if i + 1 < n and s[i] != s[i + 1]:
                    p1[i] = i
                else:
                    p1[i] = p1[i + 1]
                if i + 2 < n and s[i] != s[i + 2]:
                    p2[i] = i
                else:
                    p2[i] = p2[i + 1]
        pal = manacher(n, s)
        for _ in range(q):
            l, r = map(int, input().split())
            l -= 1
            r -= 1
            length = r - l + 1
            if p1[l] >= r:
                print(0)
                continue
            if p2[l] >= r - 1:
                k = length // 2
                print(k * (k + 1))
                continue
            ans = length * (length + 1) // 2 - 1
            if pal[l + r] >= length // 2:
                ans -= length
            print(ans)

if __name__ == "__main__":
    main()