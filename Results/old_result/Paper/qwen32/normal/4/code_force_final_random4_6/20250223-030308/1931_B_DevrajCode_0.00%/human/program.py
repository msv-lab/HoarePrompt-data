def make_equal(n, a):
    total_water = sum(a)
    
    # If total water isn't divisible by n, equal distribution isn't possible
    if total_water % n != 0:
        return 'No'
    
    target = total_water // n
    container = 0  # Tracks the net water that needs to be redistributed
    
    # Traverse through the containers
    for water in a:
        container += water - target
        # If at any point the redistribution fails, return 'No'
        if container < 0:
            return 'No'
    
    return 'Yes'
 
# Input reading optimized
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
a = list(map(int, data[1:]))
 
# Output the result
print(make_equal(n, a))