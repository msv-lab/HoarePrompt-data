from heapq import heappush, heappop

# Read the number of test cases
t = int(input())

for _ in range(t):
    # Read the number of messages and the time limit
    n, l = map(int, input().split())
    
    # Dictionary to store reading times of messages
    a_ele = {}
    # List to store transition times and their indices
    b = []
    
    # Read each message's characteristics
    for idx in range(n):
        a_1, b_1 = map(int, input().split())
        a_ele[idx] = a_1
        b.append((b_1, idx))
    
    # Sort the transition times
    b.sort()
    
    # Initialize the maximum number of messages that can be read
    ans = 0
    
    # Check if any single message can be read within the time limit
    for k, v in a_ele.items():
        if v <= l:
            ans = 1
            break
    
    # Iterate over each message as a potential starting point
    for i in range(n):
        i_idx = b[i][1]
        cur_sum = a_ele[i_idx]
        heap = []
        heappush(heap, -a_ele[i_idx])  # Use negative values for max-heap behavior
        
        # Try to add subsequent messages
        for j in range(i + 1, n):
            j_idx = b[j][1]
            cur_sum += a_ele[j_idx]
            heappush(heap, -a_ele[j_idx])
            
            # Calculate the transition cost
            diff = b[j][0] - b[i][0]
            rem = l - diff
            
            # If the remaining time is non-positive, break out of the loop
            if rem <= 0:
                break
            
            # Adjust the current sum to fit within the remaining time
            while cur_sum > rem:
                cur_sum += heap[0]  # Remove the largest reading time
                heappop(heap)
            
            # Update the maximum number of messages
            ans = max(ans, len(heap))
    
    # Output the result for the current test case
    print(ans)