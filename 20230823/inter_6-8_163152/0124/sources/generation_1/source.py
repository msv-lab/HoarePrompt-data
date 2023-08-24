def happy_grapes(x, y, z, a, b, c):
    # Check if there are enough grapes for each person
    if a >= x and b >= y and c >= z:
        # Distribute the grapes to Andrew, Dmitry, and Michal
        a -= x
        b -= y
        c -= z

        # Check if Andrew can eat all the remaining green grapes
        if a >= 0:
            # Check if Dmitry can eat all the remaining purple and green grapes
            if b + a >= 0:
                return "YES"
    return "NO"

x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

print(happy_grapes(x, y, z, a, b, c))