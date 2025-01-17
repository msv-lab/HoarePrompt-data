
for _ in range(int(input())):
    input()
    ai = [int(a) for a in input().split()]
    ni = [int(n) for n in input().split()]

    for n in ni:
        for i in range(len(ai)):
            l = len(ai)-i
            a = ai[-(i+1)]

            if n < a:
                continue

            lo = 0
            hi = n
            while lo < hi:
                mid = (lo+hi)//2
                if n - l*mid >= a:
                    lo = mid + 1
                else:
                    hi = mid

            n = n - lo*l

        print(n, end=' ')
    print('')


