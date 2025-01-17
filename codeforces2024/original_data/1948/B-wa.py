
t = int(input())
for _ in range(t):
    n =  int(input()) 
    arr = map(int, input().split())
    arr = [0] + list(arr)
    n = len(arr)
    dp = [False]*n
    dp[0] = True
    
    def check(prev , num):
        integers = list(map(int, str(num)))
        for i in range(len(integers)):
            
            if integers[i] < prev:
                return False
            prev = integers[i]
        return True
    for i in range(1, n ):
        dp[i] = dp[i - 1] & (check(arr[i - 1] % 10, arr[i]) | (arr[i] > arr[i - 1]))
        
        if dp[i] == False:
            break
    print("YES" if dp[-1] else "NO")
        