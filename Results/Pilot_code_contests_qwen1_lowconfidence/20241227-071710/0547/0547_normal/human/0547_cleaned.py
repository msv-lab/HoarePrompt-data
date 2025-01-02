try:
    (n, k) = raw_input().split()
    (n, k) = (int(n), int(k))
    nums = raw_input().split()
    nums = [int(num) for num in nums]
    nums.sort(cmp=lambda a, b: b % 10 - a % 10)
    stop = False
    while not stop:
        stop = True
        for i in range(0, n):
            if k == 0:
                break
            if nums[i] == 100:
                continue
            delta = 10 - nums[i] % 10
            if k < delta:
                break
            stop = False
            nums[i] = nums[i] + delta
            k = k - delta
    print(sum([num / 10 for num in nums]))
except IOError:
    pass