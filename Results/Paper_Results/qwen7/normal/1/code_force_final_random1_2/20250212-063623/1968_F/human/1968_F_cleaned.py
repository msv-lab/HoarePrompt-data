input = sys.stdin.read

def func_1():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        q = int(data[idx + 1])
        idx += 2
        a = [0] * (n + 1)
        pf = [0] * (n + 1)
        mp = {0: [0]}
        for i in range(1, n + 1):
            a[i] = int(data[idx])
            idx += 1
            pf[i] = pf[i - 1] ^ a[i]
            if pf[i] not in mp:
                mp[pf[i]] = []
            mp[pf[i]].append(i)
        for _ in range(q):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
            x = pf[r] ^ pf[l - 1]
            if x == 0:
                results.append('YES')
                continue
            v1 = mp.get(pf[r], [])
            v2 = mp.get(pf[l - 1], [])
            it1 = bisect.bisect_left(v1, l)
            it2 = bisect.bisect_left(v2, r) - 1
            if it1 < len(v1) and it2 >= 0 and (v1[it1] <= r) and (v2[it2] >= l):
                results.append('YES')
            else:
                results.append('NO')
        results.append('')
    print('\n'.join(results))
if __name__ == '__main__':
    func_1()