s=str(input())
if(int(s)%25==0):
  print(0)
else:
  zero=s.count('0')
  five=s.count('5')
  two = s.count('2')
  seven = s.count('7')
  # print(zero,five,two,seven)
  fin=10**18
  if(zero>=2):
    t=list(s)
    n=len(t)
    ans = 0
    cnt=0
    for i in xrange(n-1,-1,-1):
      if(t[i]=='0'):
        if(cnt==0):
          ans+=(n-1-i)
          cnt+=1
        elif(cnt==1):
          ans+=(n-2-i)
          cnt+=1
          break
    fin=min(fin,ans)
  if(two>=1 and five>=1):
    t=list(s)
    n=len(t)
    ans=0
    for i in xrange(n-1,-1,-1):
      if(t[i]=='5'):
        break
    for j in xrange(i,n-1):
      ans+=1
      temp=t[j+1]
      t[j+1]=t[j]
      t[j]=temp;
    # print(ans,t)
    for i in xrange(n-2,-1,-1):
      if(t[i]=='2'):
        break
    # print(i)
    for j in xrange(i,n-2):
      ans+=1
      temp=t[j+1]
      t[j+1]=t[j]
      t[j]=temp
    # print(ans)
    if(t[0]=='0'):
      if(n==3):
        ans = 10**15
      else:
        for i in xrange(n-3):
          if(t[i]!='0'):
            break
          ans+=1
    # print(t,ans)
    fin=min(fin,ans)



  if(seven>=1 and five>=1):
    t=list(s)
    n=len(t)
    ans=0
    for i in xrange(n-1,-1,-1):
      if(t[i]=='5'):
        break
    for j in xrange(i,n-1):
      ans+=1
      temp=t[j+1]
      t[j+1]=t[j]
      t[j]=temp;
    # print(ans,t)
    for i in xrange(n-2,-1,-1):
      if(t[i]=='7'):
        break
    # print(i)
    for j in xrange(i,n-2):
      ans+=1
      temp=t[j+1]
      t[j+1]=t[j]
      t[j]=temp
    # print(ans)
    if(t[0]=='0'):
      if(n==3):
        ans = 10**15
      else:
        for i in xrange(n-3):
          if(t[i]!='0'):
            break
          ans+=1
    # print(t,ans)
    fin=min(fin,ans)

  if(zero>=1 and five>=1):
    t=list(s)
    n=len(t)
    ans=0
    for i in xrange(n-1,-1,-1):
      if(t[i]=='0'):
        break
    for j in xrange(i,n-1):
      ans+=1
      temp=t[j+1]
      t[j+1]=t[j]
      t[j]=temp;
    # print(ans,t)
    for i in xrange(n-2,-1,-1):
      if(t[i]=='5'):
        break
    # print(i)
    for j in xrange(i,n-2):
      ans+=1
      temp=t[j+1]
      t[j+1]=t[j]
      t[j]=temp
    # print(ans)
    if(t[0]=='0'):
      if(n==3):
        ans = 10**15
      else:
        for i in xrange(n-3):
          if(t[i]!='0'):
            break
          ans+=1
    # print(t,ans)
    fin=min(fin,ans)
  if(fin>10**10):
    print(-1)
  else:
    print(fin)
    