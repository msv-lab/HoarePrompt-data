t = int(input())
# t = 1
for _ in range(0,t):
    n,c,d = [int(x) for x in input().strip().split()]
    nums = [int(x) for x in input().split()]
    nums.sort()
    orders = []

    for i in range(0,n):
        for j in range(0,n):
            orders.append(i*c + d*j + nums[0])
    # print('orders', orders)
    # print('nums', nums)
    if sorted(orders) == sorted(nums):
        print('YES')
    # if orders == nums:
    else:
        print('NO')