N = int(input())
listL = [int(i) for i in raw_input().split()]
maxL = max(listL)
sum = 0
for i in range(N):
    sum = sum + listL[i]
sum = sum - maxL
if maxL < sum:
    print('Yes')
else:
    print('No')