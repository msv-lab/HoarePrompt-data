import sys
input = sys.stdin.readline
n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append([a,b])

l.sort(key = lambda x: x[1])
# print(l)
i = 0
j = n-1
ans = 0
cnt = 0
while i <= j:
    # print(i,j,cnt,ans)
    if i == j:
        e1 = l[i][0]
        e2 = l[i][1]
        if cnt >= e1:
            ans += e1
            break

        diff = e2-cnt
        if diff < e1:
            l[i][0] -= diff
            ans += (diff * 2)
            cnt += diff
            ans += (l[i][0])
            cnt += (l[i][0])
            break

        else:
            diff = e1
            ans += (diff * 2)
            cnt += diff
            break

    else:
        if cnt >= l[i][1]:
            req = l[i][0]
            ans += req
            cnt += req
            i += 1

        else:
            diff = l[i][1]-cnt
            if diff > l[j][0]:
                 diff = l[j][0]
                 l[j][0] = 0
                 ans += (diff* 2)
                 cnt += diff
                 j -= 1

            else:
                l[j][0] -= diff
                ans += (diff*2)
                cnt += diff
                req = l[i][0]
                ans += req
                cnt += req
                if l[j][0] == 0:
                    j -= 1

                i += 1

sys.stdout.write(str(ans)+"\n")