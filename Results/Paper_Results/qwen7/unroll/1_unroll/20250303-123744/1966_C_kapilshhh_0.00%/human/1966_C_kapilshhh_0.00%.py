tc = int(input())
 
while tc > 0:
    n = int(input())
    arr = sorted(list(set([int(x) for x in input().split(' ')])), reverse=True) + [0]
    dp = True
    n = len(arr) - 1
    for i in range(1, len(arr)):
        dp = (arr[i] - (arr[i+1] if i < n else 0) > 1) or (not dp)
    print('Alice' if dp else 'Alice')
    tc -= 1