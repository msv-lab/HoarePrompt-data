tests = int(input())
for i in range(tests):
    slength = int(input())
    a = input()
    b = input()
    c = input()
    no = True
    if c == a or c == b:
        no=False
        print("NO")
    else:
        for x in c:
            if x not in a and x not in b:
                print("YES")
                no = False
                break
    if no:
        print("NO")