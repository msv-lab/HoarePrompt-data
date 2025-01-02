from __future__ import print_function;
n=input();
str=raw_input();
arr=raw_input().split();
arr=map(eval,arr);

MOD=1e9+7;
dp=[0]*3200;
dp[0]=1;
lastMatch=[0]*3200;
for i in range(len(lastMatch)) :
	lastMatch[i]=i;
maxSubLen=0;
for i in range(1,len(str)+1) :
	j=1;
	k=arr[ord(str[i-1])-ord('a')];
	while j<=k and i-j>=0 :
		maxSubLen=max(j,maxSubLen);
		dp[i]=(dp[i]+dp[i-j])%MOD;
		t=i-j-1;
		lastMatch[t+1]=max(lastMatch[t+1],i-1);
		t=t if t>0 else 0;
		k=min(k,arr[ord(str[t])-ord('a')]);
		j+=1;	
lastIndex=0;
lastStrIndex=len(str)-1;
subNum=0;
while lastIndex!=lastStrIndex :
	subNum+=1;
	if lastIndex==lastMatch[lastIndex] :
		lastIndex+=1;
	else :
		lastIndex=lastMatch[lastIndex];

print(dp[len(str)],maxSubLen,subNum,sep='\n');
