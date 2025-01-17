for _ in range(int(input())):
    r = input().split(' ')
    a, b, c = int(r[0]), int(r[1]), int(r[2])

    cen = 0
    if a > 0:
        gen = a * 2 - a + 1
        if gen == c:
            gen = 2
            cen = 0
            a -= 1
            while True:
                if a > gen:
                    cen += 1
                    gen *= 2
                    a -= gen
                elif a < gen:
                    break
                else:
                    cen += 1
                    gen *= 2
                    a = 0
                    break
            if a > 0:
                b = b - gen + a
                if b <=0:
                    cen += 2
                    print(cen)
                else:
                    cen += b // gen
                    if b % gen:
                        cen += 1
                    cen += 1
                    print(cen)
            else:
                cen += b // gen
                if b % gen:
                    cen += 1
                cen += 1
                print(cen)
        else:
            print('-1')
    else:
        if c == 1:
            print(b)
        else:
            print('-1')