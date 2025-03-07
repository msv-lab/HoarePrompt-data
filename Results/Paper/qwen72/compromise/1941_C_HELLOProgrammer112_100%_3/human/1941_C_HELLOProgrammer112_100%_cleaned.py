for _ in range(int(input())):
    a = int(input())
    s = input()
    x = s.count('map')
    y = s.count('pie')
    z = s.count('mapie')
    print(x + y - z)