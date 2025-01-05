if __name__ == "__main__":
    t=int(input())
    while(t>0):
        t-=1
        n=int(input())
        arr=input().split()
        arr=[int(arr[i]) for i in range(n)]
        ct1,ans=0,1
        for i in range(n):
            t1,t2=int(arr[i]/10),arr[i]%10
            if(t1==0):
                if(arr[i]<ct1):
                    ans=0
                    break
                else:
                    ct1=arr[i]
            elif(ct1<=t1 and t1<=t2):
                ct1=t2
            elif(ct1<=arr[i]):
                ct1=arr[i]
            else:
                ans=0
                break
        if(ans):
            print('yes')
        else:
            print('no')
