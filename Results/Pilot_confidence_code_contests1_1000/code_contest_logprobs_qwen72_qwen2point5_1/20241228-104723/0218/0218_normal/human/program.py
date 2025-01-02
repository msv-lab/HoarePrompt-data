from collections import Counter
t=int(input())
for i in range(t):
    n,k,d=map(int,raw_input().split())
    arr=list(map(int,raw_input().split()))

    def solve(arr,n,k,d):
        if n==d:
            return len(set(arr))
        m=float('inf')
        freq=Counter(arr[:d])


        for i in range(1,n-d+1):

            freq[arr[i-1]]-=1
            if freq[arr[i-1]]==0:
                del freq[arr[i-1]]

            if arr[i+d-1] in freq:
                freq[arr[i+d-1]]+=1
            else:
                freq[arr[i+d-1]]=1
            m=min(m,len(freq))

        return m

    print(solve(arr,n,k,d))

