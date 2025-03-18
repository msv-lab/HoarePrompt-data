if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        (n, m) = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a1 = 0
        a2 = n - 1
        b1 = 0
        b2 = m - 1
        ans = 0
        b.sort()
        a.sort()
        while a1 <= a2:
            dif1 = abs(a[a1] - b[b1])
            dif2 = abs(a[a1] - b[b2])
            dif3 = abs(a[a2] - b[b1])
            dif4 = abs(a[a2] - b[b2])
            if dif1 > dif2:
                if dif3 > dif4:
                    if dif3 > dif1:
                        ans += dif3
                        a2 -= 1
                        b1 += 1
                    else:
                        ans += dif1
                        a1 += 1
                        b1 += 1
                elif dif4 > dif1:
                    ans += dif4
                    a2 -= 1
                    b2 -= 1
                else:
                    ans += dif1
                    a1 += 1
                    b1 += 1
            elif dif3 > dif4:
                if dif3 > dif2:
                    ans += dif3
                    a2 -= 1
                    b1 += 1
                else:
                    ans += dif2
                    a1 += 1
                    b2 -= 1
            elif dif4 > dif2:
                ans += dif4
                a2 -= 1
                b2 -= 1
            else:
                ans += dif2
                a1 += 1
                b2 -= 1
        print(ans)