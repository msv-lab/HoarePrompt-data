n = int(input())
arr = list(map(int, input().split()))
arr.sort()
mex = 1
for num in arr:
    if num == mex:
        mex += 1
    elif num > mex:
        break
print(mex)
