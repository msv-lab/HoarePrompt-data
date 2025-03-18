def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = 0
        b = ''
        for j in range(n):
            s = input()
            if s.count('1') == 1:
                a = 'Triangle'
            elif s.count('1') > 1:
                b = 'Square'
        if a != 0:
            print(a)
        else:
            print(b)

