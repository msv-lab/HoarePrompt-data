data = list(map(int, raw_input().split()))
n = data[0]
m = data[1]
k = data[2]
nums = list(map(int, raw_input().split()))
curr = 0
offset = 0
i = 0
op = 0
while i < m:
    if nums[i] <= offset + curr * k + k:
        while i < m and nums[i] <= offset + curr * k + k:
            i += 1
        offset = i
        op += 1
    else:
        curr += (nums[i] - (offset + curr * k) - 1) / k
print(op)