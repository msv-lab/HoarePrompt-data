n = input()

d = []

for _ in range(n):
    d.append({'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0})
    for i in raw_input().split(" "):
        d[-1][i] = 1

i = -1
while(i < 10**n):
    i += 1
    ns = str(i+1)

    if n==1:
        if len(ns) == 1:
            if d[0][ns[0]] == 1:
                continue
            else:
                break
        else:
            break
    elif n==2:
        if len(ns) == 1:
            if d[0][ns[0]] == 1:
                continue
            elif d[1][ns[0]] == 1:
                continue
            else:
                break
        elif len(ns) == 2:
            if d[0][ns[0]] == 1 and d[1][ns[1]] == 1:
                continue
            elif d[1][ns[0]] == 1 and d[0][ns[1]] == 1:
                continue
            else:
                break
        else:
            break

    elif n==3:
        if len(ns) == 1:
            if d[0][ns[0]] == 1:
                continue
            elif d[1][ns[0]] == 1:
                continue
            elif d[2][ns[0]] == 1:
                continue
            else:
                break
        elif len(ns) == 2:
            if d[0][ns[0]] == 1 and (d[1][ns[1]] == 1 or d[2][ns[1]] == 1):
                continue
            elif d[1][ns[0]] == 1 and (d[0][ns[1]] == 1 or d[2][ns[1]] == 1):
                continue
            elif d[2][ns[0]] == 1 and (d[1][ns[1]] == 1 or d[0][ns[1]] == 1):
                continue
            else:
                break
        elif len(ns) == 3:
            if d[0][ns[0]] == 1 and d[1][ns[1]] == 1 and d[2][ns[2]] == 1:
                continue
            elif d[0][ns[0]] == 1 and d[2][ns[1]] == 1 and d[1][ns[2]] == 1:
                continue
            elif d[1][ns[0]] == 1 and d[0][ns[1]] == 1 and d[2][ns[2]] == 1:
                continue
            elif d[1][ns[0]] == 1 and d[2][ns[1]] == 1 and d[0][ns[2]] == 1:
                continue
            elif d[2][ns[0]] == 1 and d[1][ns[1]] == 1 and d[0][ns[2]] == 1:
                continue
            elif d[2][ns[0]] == 1 and d[0][ns[1]] == 1 and d[1][ns[2]] == 1:
                continue
            else:
                break
        else:
            break

print(i)

