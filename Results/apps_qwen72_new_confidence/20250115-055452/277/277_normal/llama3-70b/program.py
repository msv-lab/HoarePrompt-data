n = int(input())
arr = []
for i in range(n):
    arr.append(input())

lis = ['purple','green','blue','orange','red','yellow']
st = ['Power','Time','Space','Soul','Reality','Mind']
ans = []
for i in range(len(lis)):
    if lis[i] not in arr:
        ans.append(st[i])

print(len(ans))
for i in range(len(ans)):
    print(ans[i])