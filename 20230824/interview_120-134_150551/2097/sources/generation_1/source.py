t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    steps = 0
    
    # Check if the sum and product are already non-zero
    if sum(a) != 0 and 0 not in a:
        print(0)
        continue
    
    # Count the number of zeros in the array
    zeros = a.count(0)
    
    # If there are more than one zero, increase the count of steps by 1
    if zeros >= 2:
        steps += 1
    
    # If there is only one zero, increase the count of steps by 2
    elif zeros == 1:
        steps += 2
    
    print(steps)