n = int(input())
 
for _ in range(n):
    m = int(input())
    arr = [int(i) for i in input().split()]
    ans = True
    for i in range(m-1, 0, -1):
        if arr[i] < arr[i-1]:
            nums = [int(i) for i in str(arr[i-1])] + [arr[i]]
            if nums != sorted(nums):
                ans = False;break;
            arr[i-1] = nums[0]
    print(["NO","YES"][ans])