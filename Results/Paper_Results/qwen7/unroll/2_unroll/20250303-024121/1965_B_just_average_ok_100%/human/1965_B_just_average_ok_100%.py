for _ in range(int(input())):
    n, k = map(int, input().split())
    
    nums = [(1<<i) for i in range(21)]
    idx = -1
    for i in range(len(nums)):
        if nums[i] > k:
            idx = i-1
            break
    nums.append(k-nums[idx])
    nums.append(k+1)
    nums.append(k+nums[idx]+1)
    nums.remove(1 << idx)
    print(len(nums))
    print(*nums)