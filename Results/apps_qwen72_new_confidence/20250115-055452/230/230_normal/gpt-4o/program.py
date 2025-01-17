def can_make_equal(arr):
    # Get unique elements
    unique_elements = list(set(arr))
    
    # If there's only 1 unique element, it's already all equal
    if len(unique_elements) == 1:
        return "YES"
    
    # If there are more than 3 unique elements, it's impossible
    if len(unique_elements) > 3:
        return "NO"
    
    # If there are exactly 3 unique elements
    if len(unique_elements) == 3:
        unique_elements.sort()
        # Check if the middle element is the average of the other two
        if unique_elements[1] - unique_elements[0] == unique_elements[2] - unique_elements[1]:
            return "YES"
        else:
            return "NO"
    
    # If there are exactly 2 unique elements, it's always possible
    return "YES"

# Read input from standard input
import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
array = list(map(int, data[1:n+1]))

print(can_make_equal(array))
