def func_1():
    count = 0
    flag = 0
    while True:
        a = sys.stdin.read(1)
        if a == '/':
            if flag == 0:
                flag = 1
            else:
                pass
        elif a == '\n':
            break
        else:
            if flag == 1:
                sys.stdout.write('/')
            count += 1
            sys.stdout.write(a)
            flag = 0
    if not count:
        sys.stdout.write('/')
if __name__ == '__main__':
    func_1()