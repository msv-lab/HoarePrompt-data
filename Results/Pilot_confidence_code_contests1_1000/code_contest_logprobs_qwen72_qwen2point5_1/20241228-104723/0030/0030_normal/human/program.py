a, n = map(int, raw_input().split())
bs = map(int, raw_input().split())
bs = sorted(bs, reverse=True)
for b in bs:
    if(n%b==0):
        print(n/b)
        exit(0)
