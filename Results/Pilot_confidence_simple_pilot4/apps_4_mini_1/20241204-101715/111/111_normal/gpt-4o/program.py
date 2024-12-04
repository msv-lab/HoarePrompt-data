def maximize_array_product():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:]))

    for i in range(n):
        if a[i] >= 0:
            a[i] = -a[i] - 1

    if n % 2 != 0:
        min_index = 0
        for i in range(1, n):
            if a[i] > a[min_index]:
                min_index = i
        a[min_index] = -a[min_index] - 1

    print(" ".join(map(str, a)))

# Call the function to execute the program
maximize_array_product()
