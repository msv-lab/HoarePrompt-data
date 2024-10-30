import math

def minimal_angle_vectors():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    vectors = []
    
    for i in range(n):
        x = int(data[2*i + 1])
        y = int(data[2*i + 2])
        angle = math.atan2(y, x)
        vectors.append((angle, i + 1))
        
    vectors.sort()
    
    min_angle = float('inf')
    a, b = -1, -1
    
    for i in range(1, n):
        angle_diff = vectors[i][0] - vectors[i - 1][0]
        if angle_diff < min_angle:
            min_angle = angle_diff
            a, b = vectors[i - 1][1], vectors[i][1]
            
    # Check the circular case, between the first and last vector
    first_last_angle_diff = 2 * math.pi - (vectors[-1][0] - vectors[0][0])
    if first_last_angle_diff < min_angle:
        a, b = vectors[0][1], vectors[-1][1]
    
    print(a, b)

minimal_angle_vectors()
