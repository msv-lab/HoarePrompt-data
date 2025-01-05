n = int(sys.stdin.readline().rstrip('\n'))
change = 1000000
nom = [1]
if n <= 10:
    for x in range(1000001 - 1, 0, -1):
        if len(nom) == n:
            break
        nom.append(x)
elif 10 < n <= 100:
    res = n - n % 10 - 1
    res_ = change // res
    nom.append(res_)
    for x in range(1000000 - 1, 0, -1):
        if len(nom) == 10:
            break
        nom.append(x)
elif 100 < n <= 1000:
    res = n - n % 10 - 1
    res_ = change // res
    nom.append(res_)
    for x in range(1000000 - 1, 0, -1):
        if len(nom) == 10:
            break
        elif len(nom) == n % 10 + 2:
            break
        nom.append(x)
elif 1000 < n <= 10000:
    if n == 10000:
        change = 10000
        print(str(change) + ' ' + str(2))
        print(str(1) + ' ' + str(9))
        exit(0)
    res = n - n % 10 - 1
    res_ = change // res
    nom.append(res_)
    for x in range(1000000 - 1, 0, -1):
        if len(nom) == 10:
            break
        elif len(nom) == n % 10 + 2:
            break
        nom.append(x)
elif 10000 < n <= 100000:
    if n == 100000:
        change = 100000
        print(str(change) + ' ' + str(2))
        print(str(1) + ' ' + str(9))
        exit(0)
    res = n - n % 10 - 1
    res_ = change // res
    nom.append(res_)
    for x in range(1000000 - 1, 0, -1):
        if len(nom) == 10:
            break
        elif len(nom) == n % 10 + 2:
            break
        nom.append(x)
print(str(change) + ' ' + str(len(nom)))
print(' '.join(list(map(str, nom))))
exit(0)