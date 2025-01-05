import heapq

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of mushrooms
    n = int(input())
    
    # Read the magic powers of the mushrooms
    v = list(map(int, input().split()))
    
    # Read the permutation
    p = list(map(int, input().split()))
    
    # Calculate the maximum size of the initial heap
    max_size = (n + 2) // 2
    
    # Initialize a min-heap
    h = []
    heapq.heapify(h)
    
    # Fill the heap with the largest possible subset of mushrooms
    for j in range(max_size):
        heapq.heappush(h, v[p[n - 1 - j] - 1])
    
    # If n is even, pop one element to adjust the heap size
    if n % 2 == 0:
        heapq.heappop(h)
    
    # Initialize the output with the current heap configuration
    output = (len(h) * h[0], len(h))
    
    # Iterate to find the optimal configuration
    while True:
        if len(h) == 1:
            # If only one mushroom is left, check if it gives a better result
            if h[0] >= output[0]:
                output = (h[0], 1)
            break
        else:
            # Pop the smallest element from the heap
            heapq.heappop(h)
            l = len(h)
            
            # Check if the next mushroom in the permutation can improve the heap
            if h[0] < v[p[l - 1] - 1]:
                heapq.heappop(h)
                heapq.heappush(h, v[p[l - 1] - 1])
            
            # Update the output if the current configuration is better
            if h[0] * l >= output[0]:
                output = (h[0] * l, l)
    
    # Print the result for the current test case
    print(output[0], output[1])