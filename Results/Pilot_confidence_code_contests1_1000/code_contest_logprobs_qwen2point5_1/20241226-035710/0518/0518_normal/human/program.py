while(True):
    n = input()
    if(n == 0):
        break
    ans = 0
    a = 5
    count = 0
    while(True):
        count = n / a
        if(count == 0):
            break
        ans += count
        a *= 5
    print(ans)