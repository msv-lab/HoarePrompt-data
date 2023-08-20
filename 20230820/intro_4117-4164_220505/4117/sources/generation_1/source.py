def count_triangles(N, lengths):
    count = 0
    
    # Iterate over all possible combinations of three sticks
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                # Check if the lengths of the sticks are all different and can form a triangle
                if lengths[i] != lengths[j] and lengths[j] != lengths[k] and lengths[k] != lengths[i]:
                    if lengths[i] + lengths[j] > lengths[k] and lengths[j] + lengths[k] > lengths[i] and lengths[k] + lengths[i] > lengths[j]:
                        count += 1
    
    return count

# Read the input
N = int(input())
lengths = list(map(int, input().split()))

# Call the function and print the result
result = count_triangles(N, lengths)
print(result)