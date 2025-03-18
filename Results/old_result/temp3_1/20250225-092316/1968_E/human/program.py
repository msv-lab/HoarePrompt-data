def func():
    t = int(input())
    while t:
        t -= 1
        n = int(input())
        print(n, end=' ')
        print(n)
        print(n, end=' ')
        print(n - 1)
        if n == 3:
            print(2, end=' ')
            print(1)
        else:
            for i in range(1, n - 1):
                print(i, end=' ')
                print(i)
        print(' ')

