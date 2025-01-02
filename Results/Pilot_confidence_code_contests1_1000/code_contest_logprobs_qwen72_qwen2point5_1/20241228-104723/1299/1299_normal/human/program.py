n = int(raw_input())
train = list(map(int,raw_input().split()))
start = [9999]*5001
end = [0]*5001
for i in range(n):
    elm = train[i]
    start[elm] = min(start[elm], i)
    end[elm] = max(end[elm], i)

segstart = [(-float('inf'), -1)]*n # if I make a segment starting from i (if possible), the xor value and endpoint
for i in range(n):
    elm = train[i]
    if start[elm] != i: continue
    if start[elm] == end[elm]:
        segstart[i] = (elm, i)
        continue
    j = i
    endpoint = end[elm]
    xorval = 0
    while j < endpoint:
        if j == start[train[j]]:
            endpoint = max(endpoint, end[train[j]])
            xorval^= train[j]
        elif start[train[j]] < i:
            break
        j+= 1
    else:
        segstart[i] = (xorval, j)
dp = [0]*n # optimal value for 0..i
for i in range(n):
    dp[i] = max(dp[i], dp[max(0,i-1)])
    xorval, j = segstart[i]
    if j == -1: continue
    dp[j] = max(dp[j], dp[max(0,i-1)]+xorval)
print(dp[-1])