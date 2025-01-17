for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    
    tot = 0
    check = False
    for x in nums:
        if x%3 == 1 or n==1:
            check = True
        tot += x

    if tot%3 == 0:
        print(0)
    elif tot%3 == 2:
        print(1)
    else:
        if check:
            print(1)
        else:
            print(2)
