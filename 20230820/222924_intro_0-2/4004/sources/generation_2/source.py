n = int(input())
a = list(map(int, input().split()))

# Find the minimum and maximum values in the array
min_a = min(a)
max_a = max(a)

# If all elements are already equal, we don't need to make any changes
if min_a == max_a:
    print(0)
else:
    # Check if it is possible to make all elements equal by adding or subtracting a certain amount
    possible_values = set([(max_a - min_a) // (n-1) * i + min_a for i in range(n)])
    
    # Check if any of the possible values make all elements equal
    for value in possible_values:
        if all((ai - value) % (value - min_a) == 0 or (ai - min_a) % (value - min_a) == 0 for ai in a):
            print(value - min_a)
            exit()
    
    # If no such value exists, it is impossible to make all elements equal
    print(-1)
    