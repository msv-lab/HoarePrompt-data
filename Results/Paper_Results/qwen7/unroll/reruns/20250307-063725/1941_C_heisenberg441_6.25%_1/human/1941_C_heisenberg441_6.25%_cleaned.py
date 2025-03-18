def func_1(s):
    if s == 'mapie':
        return 1
    ans = 0
    while s.find('map') != -1:
        s = s[:s.find('map')] + s[s.find('map') + 2:]
        ans += 1
    while s.find('pie') != -1:
        s = s[:s.find('pie')] + s[s.find('pie') + 2:]
        ans += 1
    return ans
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(func_1(s))