num_tests = int(input())
 
while num_tests > 0:
    num_tests -= 1
 
    n = int(input())
    nums = [int(x) for x in input().split(" ")] 
 
    start_year = 0
    for x in range(0, len(nums)):
        start_year = ((start_year)//nums[x] + 1)*(nums[x])
    print(start_year)