def maximum_pairs(n, sequences):
    stack = []  # stack to store the indices of opening brackets
    pair_count = 0  # count of pairs formed
    
    for seq in sequences:
        for i, char in enumerate(seq):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if len(stack) > 0:
                    stack.pop()
                    pair_count += 1
    
    return pair_count // 2

# Read input values
n = int(input())
sequences = []
for _ in range(n):
    sequences.append(input())

# Call the function and print the result
print(maximum_pairs(n, sequences))