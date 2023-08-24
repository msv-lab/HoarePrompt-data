# Read the inputs
n = int(input())
passengers = list(map(int, input().split()))
order = list(map(int, input().split()))

# Initialize variables
segments = 1
chaos = 0
max_chaos = 0

# Loop through the order of blowing up coaches
for i in range(n):
    # Get the index of the coach to blow up
    coach_idx = order[i] - 1
    
    # Update the chaos and segments
    chaos += passengers[coach_idx]
    segments += 1
    
    # Calculate the chaos of the current segment
    segment_chaos = (sum(passengers[:i+1]) + 9) // 10
    
    # Calculate the maximum chaos so far
    max_chaos = max(max_chaos, segment_chaos * segments)

# Print the maximum chaos
print(max_chaos)