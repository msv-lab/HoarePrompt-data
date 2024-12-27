def main():
    n = int(raw_input())
    l = []
    r = []
    for i in range(n):
        li,ri = map(int, raw_input().split())
        l.append(li)
        r.append(ri)
    res = min(n - sum(l),sum(l)) + min(n - sum(r),sum(r))
    print(res)

main()