n = int(input())
candies = []
for _ in range(n):
    candies.append(int(input()))

candies.sort()

if n == 0:
    print("YES")
    print(1)
    print(1)
    print(3)
    print(3)
elif n == 1:
    print("YES")
    print(candies[0])
    print(3 * candies[0])
    print(3 * candies[0])
elif n == 2:
    a = candies[0]
    b = candies[1]
    if (a + b) % 2 != 0:
        print("NO")
    else:
        c = (a + b) // 2
        
        if 3 * c >= 1000000:
            print("NO")
        else:
            print("YES")
            print(3 * c)
            print(3 * c)
elif n == 3:
    a = candies[0]
    b = candies[1]
    c = candies[2]
    
    if (a + c) % 2 != 0:
        print("NO")
    elif b >= c or a >= b:
        print("NO")
    else:
        median = (a + c) // 2
        if median - b + c >= 1000000:
            print("NO")
        else:
            print("YES")
            print(median - b + c)
elif n == 4:
    a = candies[0]
    b = candies[1]
    c = candies[2]
    d = candies[3]
    
    if (a + d) % 2 != 0:
        print("NO")
    elif b >= c or a >= b or c >= d:
        print("NO")
    else:
        mean = (a + b + c + d) // 4
        median = (b + c) // 2
        range_val = d - a
        
        if mean != median or median != range_val:
            print("NO")
        else:
            print("YES")
else:
    print("NO")