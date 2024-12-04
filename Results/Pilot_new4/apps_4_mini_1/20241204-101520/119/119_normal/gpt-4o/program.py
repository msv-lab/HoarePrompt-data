t, s, x = map(int, input().split())

if x == t:
    print("YES")
elif x > t:
    if (x - t) % s == 0:
        print("YES")
    elif (x - t - 1) % s == 0 and x != t + 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
