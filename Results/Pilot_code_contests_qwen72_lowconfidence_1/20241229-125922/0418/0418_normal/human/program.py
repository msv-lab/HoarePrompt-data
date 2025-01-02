




data = [[] for i in range(4)]


n,m = map(int,raw_input().split())


for i in range(0,n):
    w,c = map(int,raw_input().split())
    data[w].append(c)
#print(data)

for i in range(1,4):
    data[i].sort()
    data[i].reverse()

dp = []
for i in range(0,300010):
    dp.append((0,0,0))




for i in range(1,m+1):
    for j in range(1,3):
        if(i-j<0 or dp[i-j][j] >= len(data[j])):
            continue

        val = dp[i-j][0] + data[j][dp[i-j][j]]
        if(val > dp[i][0]):
            a0 = val
            a1 = dp[i-j][1]
            a2 = dp[i-j][2]
            if(j == 1):
                a1 += 1
            else :
                a2 += 1
            dp[i] = (a0,a1,a2)
        if(dp[i][0] < dp[i-1][0]) :
            dp[i] = dp[i-1]

ans = dp[w][0]
sum = 0

for i in range(0,len(data[3])):
    if (i+1) * 3 > w :
        break
    sum += data[3][i]
    if ans < sum + dp[w - 3 * (i+1)][0] :
        ans = sum + dp[w-3*(i+1)][0]




print(ans)

