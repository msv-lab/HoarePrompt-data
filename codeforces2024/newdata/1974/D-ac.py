t = int(input())
for _ in range(t):
    m = int(input())
    l = input()
    n, s, w, e = 0, 0, 0, 0

    for i in l:
        if i == 'N':
            n += 1
        elif i == 'S':
            s += 1
        elif i =='W':
            w += 1
        else:
            e += 1

    if n > s:
        nn, ss = n-s, 0
    else:
        nn, ss = 0, s-n
    if w > e:
        ww, ee = w-e, 0
    else:
        ww, ee = 0, e-w
    if nn%2 == 1 or ss%2 == 1 or ww%2 == 1 or ee%2 == 1:
        print('NO')
    else:
        r, h = 0, 0
        rr, hh = [0]*4, [0]*4 #nswe
        pp = []
        for i in l:
            if i == 'W':
                if ww:
                    if ww%2 == 1:
                        r += 1
                        pp.append('R')
                    else:
                        h += 1
                        pp.append('H')
                    ww -= 1
                else:
                    if rr[3]:
                        rr[3] -= 1
                        r += 1
                        pp.append('R')
                    elif hh[3]:
                        hh[3] -= 1
                        h += 1
                        pp.append('H')
                    elif r < h:
                        rr[2] += 1
                        r += 1
                        pp.append('R')
                    else:
                        hh[2] += 1
                        h += 1
                        pp.append('H')

            elif i == 'E':
                if ee:
                    if ee % 2 == 1:
                        r += 1
                        pp.append('R')
                    else:
                        h += 1
                        pp.append('H')
                    ee -= 1
                else:
                    if rr[2]:
                        rr[2] -= 1
                        r += 1
                        pp.append('R')
                    elif hh[2]:
                        hh[2] -= 1
                        h += 1
                        pp.append('H')
                    elif r < h:
                        rr[3] += 1
                        r += 1
                        pp.append('R')
                    else:
                        hh[3] += 1
                        h += 1
                        pp.append('H')

            elif i == 'N':
                if nn:
                    if nn % 2 == 1:
                        r += 1
                        pp.append('R')
                    else:
                        h += 1
                        pp.append('H')
                    nn -= 1
                else:
                    if rr[1]:
                        rr[1] -= 1
                        r += 1
                        pp.append('R')
                    elif hh[1]:
                        hh[1] -= 1
                        h += 1
                        pp.append('H')
                    elif r < h:
                        rr[0] += 1
                        r += 1
                        pp.append('R')
                    else:
                        hh[0] += 1
                        h += 1
                        pp.append('H')

            elif i == 'S':
                if ss:
                    if ss % 2 == 1:
                        r += 1
                        pp.append('R')
                    else:
                        h += 1
                        pp.append('H')
                    ss -= 1
                else:
                    if rr[0]:
                        rr[0] -= 1
                        r += 1
                        pp.append('R')
                    elif hh[0]:
                        hh[0] -= 1
                        h += 1
                        pp.append('H')
                    elif r < h:
                        rr[1] += 1
                        r += 1
                        pp.append('R')
                    else:
                        hh[1] += 1
                        h += 1
                        pp.append('H')
        if r and h:
            print(''.join(pp))
        else:
            print('NO')