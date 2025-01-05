t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n == 1 or n == 2:
        print(0)
    else:
        ans = 0
        arr1 = float("inf")
        arr2 = float("inf")
        for i in range(n):
            num = a[i]
            if num > arr2:
                arr1 = num
                ans += 1
            elif num <= arr1:
                arr1 = num
            elif num > arr1 and num <= arr2:
                arr2 = num
            else:
                continue
            arr2,arr1 = max(arr1,arr2),min(arr1,arr2)
        print(ans)

            