import math

def find_min_angle_vectors(n, vectors):
    # Convert vectors to polar angles and store the angles with original indices
    angles = []
    for i in range(n):
        x, y = vectors[i]
        angle = math.atan2(y, x)
        angles.append((angle, i + 1))
    
    # Sort the vectors based on their angles
    angles.sort()
    
    min_angle = float('inf')
    best_pair = (-1, -1)
    
    # Check consecutive vectors in the sorted list
    for i in range(n):
        # Get the current angle and the next angle (circular list)
        angle1, index1 = angles[i]
        angle2, index2 = angles[(i + 1) % n]
        
        # Calculate the difference in angles
        diff = abs(angle2 - angle1)
        if diff > math.pi:
            diff = 2 * math.pi - diff
        
        if diff < min_angle:
            min_angle = diff
            best_pair = (index1, index2)
    
    return best_pair

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
vectors = []

for i in range(n):
    x = int(data[2 * i + 1])
    y = int(data[2 * i + 2])
    vectors.append((x, y))

# Find and print the result
a, b = find_min_angle_vectors(n, vectors)
print(a, b)
