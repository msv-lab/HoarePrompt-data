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
    if (max_a - min_a) % (n-1) == 0:
        value = (max_a - min_a) // (n-1)
        
        # Check if all elements become equal after adding or subtracting the calculated value
        if all((ai - value) % value == 0 or ai == min_a for ai in a):
            print(value)
            exit()
    
    # If no such value exists, it is impossible to make all elements equal
    print(-1)