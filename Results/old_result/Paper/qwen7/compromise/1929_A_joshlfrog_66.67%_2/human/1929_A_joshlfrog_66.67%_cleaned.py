t = int(input())
for e in range(t):
    l = int(input())
    nums = [int(x) for x in input().split()]
    x = 0
    y = 100000000
    for i in range(l):
        if nums[i] > x:
            x = nums[i]
        if nums[i] < y:
            y = nums[i]
    print(x - y)