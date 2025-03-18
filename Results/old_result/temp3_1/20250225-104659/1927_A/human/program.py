def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        first_black = s.find('B')
        last_black = s.rfind('B')
        min_paint = last_black - first_black + 1
        print(min_paint)

