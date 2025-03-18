if __name__ == "__main__":
    t=int(input())
    while(t>0):
        t-=1
        [n,x,y]=map(int,input().split())
        arr=input().split()
        arr=[int(arr[i]) for i in range(x)]
        print(x-2)