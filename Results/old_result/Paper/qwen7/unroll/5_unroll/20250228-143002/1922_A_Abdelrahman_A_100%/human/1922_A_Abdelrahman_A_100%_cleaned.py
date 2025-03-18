tests = int(input())
for i in range(tests):
    slength = int(input())
    a = input()
    b = input()
    c = input()
    no = True
    if c == a or c == b:
        no = False
        print('NO')
    else:
        counter = 0
        for x in c:
            if x not in a[counter] and x not in b[counter]:
                no = False
                print('YES')
                break
            counter += 1
    if no:
        print('NO')