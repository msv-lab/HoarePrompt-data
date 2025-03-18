def func():
    for i in range(int(input())):
        x = int(input())
        max = 100000000
        min = -100000000
        ans = ''
        t = 0
        while x != 1:
            if x % 2 == 0:
                ans = f'{max}' + ' ' + ans
                max -= 1
                x = x // 2
            else:
                ans = f'{min}' + ' ' + ans
                min += 1
                x -= 1
            t += 1
        print(t)
        print(*ans)

