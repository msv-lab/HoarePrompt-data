s = input()
links = s.count('-')
pearls = s.count('o')

if pearls == 0:
    print("NO")
elif links % pearls == 0:
    print("YES")
else:
    print("NO")
