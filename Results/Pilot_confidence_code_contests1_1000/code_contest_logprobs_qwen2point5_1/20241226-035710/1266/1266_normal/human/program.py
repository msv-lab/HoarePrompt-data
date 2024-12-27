N = int(raw_input())
nums = map(int, raw_input().split(" "))

count = 0
for i in range(0, len(nums)):
    for j in range(len(nums)-1, i, -1):
        if nums[j-1] > nums[j]:
            temp = nums[j-1]
            nums[j-1] = nums[j]
            nums[j] = temp
            count += 1

nums = map(str, nums)
print(" ".join(nums))
print(count)