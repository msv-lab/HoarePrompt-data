def happy_grapes(x, y, z, a, b, c):
    # Check if there are enough grapes for each person
    if a >= x and b >= y and c >= z:
        # Distribute the grapes to Andrew, Dmitry, and Michal
        a -= x
        b -= y
        c -= z

        # Check if Dmitry can eat all the remaining purple and green grapes
        if b + a >= 0:
            # Check if Michal can eat all the remaining grapes
            if c + b + a >= 0:
                return "YES"
    return "NO"

# Read the input
x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

# Call the function and print the result
print(happy_grapes(x, y, z, a, b, c))