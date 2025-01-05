t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the array
    a = list(map(int, input().split()))  # Array elements
    a.sort()  # Sort the array

    # Case 1: If 1 is in the array, the answer is "YES"
    if 1 in a:
        print("YES")
        continue

    # Case 2: If all elements are the same, the answer is "YES"
    if len(set(a)) == 1:
        print("YES")
        continue

    # Case 3: We need to check if two numbers can divide all elements
    # We check if the smallest element can divide all other elements
    first = a[0]
    possible = True

    # Check if every element is divisible by `first`
    for x in a:
        if x % first != 0:
            possible = False
            break

    if possible:
        print("YES")
    else:
        # Try checking for another divisor (second smallest element)
        second = a[1]  # This is the second smallest distinct number
        possible = True

        # Check if every element is divisible by either `first` or `second`
        for x in a:
            if x % first != 0 and x % second != 0:
                possible = False
                break

        if possible:
            print("YES")
        else:
            print("NO")

