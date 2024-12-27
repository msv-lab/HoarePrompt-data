n,k=map(int, raw_input().split())
if(n==1 and k==0):
  print(1)
elif(n==1 or k==0):
  print(-1)
elif(n//2>k):
  print(-1)
else:
  ans=[]
  nums=n//2
  needed=[k+1-nums, (k+1-nums)*2]
  curr=1
  for i in range(nums-1):
    while(curr in needed or curr+1 in needed):
      curr+=1
    ans.append(curr)
    ans.append(curr+1)
    curr+=2
  ans.append(needed[0])
  ans.append(needed[1])
  # print(len(ans))
  if(len(ans)==n):
    print(" ".join(map(str, ans)))
  else:
    ans.append(max(ans)+1)
    print(" ".join(map(str, ans)))