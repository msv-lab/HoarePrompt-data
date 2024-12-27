N = int(raw_input())
nums = [int(i) for i in raw_input().split(' ')]
zeroFound = False
output = []
zeros_after_1 = 0
for i in range(N):
    if nums[i] == 0 and zeroFound:
        zeros_after_1 += 1
    elif nums[i] == 1:
        zeroFound = True
        output.append("1")
    else:
        output.append("0")
print(len(output))
