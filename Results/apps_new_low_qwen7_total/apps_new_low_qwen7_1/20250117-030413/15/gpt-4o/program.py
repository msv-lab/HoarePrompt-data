def is_stack_sortable_starting_with_k(n, k, p):
    # Check if the given starting array is already in stack-sortable order
    stack = []
    max_seen = 0
    for num in p:
        if num < max_seen:
            return -1
        while stack and stack[-1] < num:
            max_seen = stack.pop()
        stack.append(num)

    remaining_numbers = set(range(1, n + 1)) - set(p)
    remaining_numbers = sorted(remaining_numbers, reverse=True)

    # Try to construct the remaining part of the permutation
    result = p[:]
    for num in remaining_numbers:
        while stack and stack[-1] < num:
            result.append(stack.pop())
        stack.append(num)
    
    result.extend(reversed(stack))
    
    # Verify if the constructed permutation is stack-sortable
    stack = []
    max_seen = 0
    for num in result:
        if num < max_seen:
            return -1
        while stack and stack[-1] < num:
            max_seen = stack.pop()
        stack.append(num)
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
k = int(data[1])
p = list(map(int, data[2:]))

# Solve the problem
result = is_stack_sortable_starting_with_k(n, k, p)
if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))
