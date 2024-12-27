'''
n, k = [int(s) for s in raw_input().split()]
if k == 1:
    print(0)
else:
    first = [int(s) for s in raw_input().split()]
    i = 2
    while (i < len(first)):
        if first[i] == first[i-1] + 1:
            i += 1
        else:
            break
    ans = len(first) - i
    for j in xrange(k-1):
        inp = [s for s in raw_input().split()]
        ans += int(inp[0]) - 1
    ans += n - 1
    ans -= i - 2
    print (ans)
'''
n, k = [int(s) for s in raw_input().split()]
ans = 0
if k == 1:
    print(0)
else:
    for j in xrange(k):
        inp = [s for s in raw_input().split()]
        if int(inp[1]) == 1:
            i = 2
            while (i < int(inp[0]) + 1):
                if int(inp[i]) == int(inp[i-1]) + 1:
                    i += 1
                else:
                    break
            ans += int(inp[0]) - i + 1
        else:
            ans += int(inp[0]) - 1
    ans += n - 1
    ans -= i - 2
    print (ans)

