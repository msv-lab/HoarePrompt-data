# Read input values
x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

# Check if there are enough green grapes for Andrew
if a < x:
    print("NO")
else:
    # Deduct the green grapes taken by Andrew
    a -= x

    # Check if there are enough green and purple grapes for Dmitry
    if a + b < y:
        print("NO")
    else:
        # Deduct the required grapes for Dmitry
        if a >= y:
            a -= y
        else:
            y -= a
            a = 0
            b -= y

        # Check if the remaining grapes (any color) are enough for Michal
        if a + b + c < z:
            print("NO")
        else:
            print("YES")
