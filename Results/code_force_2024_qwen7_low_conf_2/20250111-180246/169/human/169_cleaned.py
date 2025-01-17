def func_1(arr):
    num_set = set(arr)
    mex = 0
    while mex in num_set:
        mex += 1
    return mex
test_cases = int(input())
for _ in range(test_cases):
    size = int(input())
    arr = list(map(int, input().split()))
    mex = func_1(arr)
    if mex == 0:
        print(2)
        print(1, 1)
        print(2, size)
        continue
    cnt = 0
    start = 0
    segments = []
    num_set = set()
    for i in range(size):
        if arr[i] < mex:
            num_set.add(arr[i])
        if len(num_set) == mex:
            segments.append((start + 1, i + 1))
            start = i + 1
            num_set.clear()
    if num_set:
        segments[-1] = (segments[-1][0], size)
    if len(segments) < 2:
        print(-1)
    else:
        print(len(segments))
        for seg in segments:
            print(seg[0], seg[1])