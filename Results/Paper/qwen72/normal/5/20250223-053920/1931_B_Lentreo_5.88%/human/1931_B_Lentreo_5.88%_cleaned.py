t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().strip().split()))
    last = nums[-1]
    curr = 0
    for i in nums:
        if i != 0:
            curr += i - last
    if curr == 0:
        print('YES')
    else:
        print('NO')