n=input();flag=True
nums=map(int,raw_input().split())
while flag and nums:
  for i in xrange(len(nums)-1):
    if abs(nums[i]-nums[i+1])>=2:
      flag=False
      break
  nums.remove(max(nums))
print ["NO","YES"][flag]
