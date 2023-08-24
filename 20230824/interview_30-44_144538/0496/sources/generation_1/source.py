# Read input sequence
a, b, c, d = map(int, input().split())

# Check if given sequence is arithmetic progression
if b - a == c - b == d - c:
    # Compute the next element in arithmetic progression
    next_element = d + (d - c)
    # Check if next element is an integer
    if next_element % 1 != 0:
        print(42)
    else:
        print(int(next_element))
else:
    # Check if given sequence is geometric progression
    if a != 0 and b != 0 and c != 0 and d != 0:
        if b / a == c / b == d / c:
            # Compute the next element in geometric progression
            next_element = d * (d / c)
            # Check if next element is an integer
            if next_element % 1 != 0:
                print(42)
            else:
                print(int(next_element))
        else:
            print(42)
    else:
        print(42)