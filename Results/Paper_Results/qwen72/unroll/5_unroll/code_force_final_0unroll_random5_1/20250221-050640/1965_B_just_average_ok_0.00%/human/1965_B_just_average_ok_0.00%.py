for _ in range(int(input())):
    n, k = map(int, input().split())
    
    nums = [(1<<i) for i in range(24)]
    idx = 0
    while k >= (1 << idx): idx+=1
    idx -= 1
    nums.append(k-nums[idx])
    nums.append(k+1)
    nums.append(k+nums[idx]+1)
    nums.remove(1 << idx)
    print(len(nums))
    print(*nums)