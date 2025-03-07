for t in range(int(input())):
    (n, m, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    aOnes = 0
    bOnes = 0
    newk = k // 2
    i = 1
    while i <= k:
        if i in a and i in b:
            if aOnes < bOnes:
                aOnes += 1
            else:
                bOnes += 1
        elif i in a and aOnes <= newk:
            aOnes += 1
        elif i in b and bOnes <= newk:
            bOnes += 1
        else:
            break
        i += 1
    if aOnes == newk and bOnes == newk:
        print('yes')
    else:
        print('no')