for i in range(int(input())):
    n = input()
    s = input()

    cnt_u = 0
    for j in s:
        if j == "U":
            cnt_u+=1
    if cnt_u % 2 == 1:
        print('Alice')
    else:
        print('Bob')