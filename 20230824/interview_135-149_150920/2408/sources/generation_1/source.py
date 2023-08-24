
# Read the number of poles
n = int(input())

# Initialize a counter for intersecting wires
intersecting_wires = 0

# Create a list to store the coordinates of the poles
poles = []

# Read the coordinates of the poles and store them in the list
for _ in range(n):
    x, y = map(int, input().split())
    poles.append((x, y))

# Iterate through all possible pairs of poles
for i in range(n):
    for j in range(i+1, n):
        # Get the coordinates of the current pair of poles
        x1, y1 = poles[i]
        x2, y2 = poles[j]
        
        # Check if the wires formed by the current pair of poles intersect with any other wire
        for k in range(n):
            for l in range(k+1, n):
                # Skip the current pair of poles being checked
                if (k == i and l == j) or (k == j and l == i):
                    continue
                
                # Get the coordinates of the other pair of poles
                x3, y3 = poles[k]
                x4, y4 = poles[l]
                
                # Check if the wires intersect
                if intersect((x1, y1), (x2, y2), (x3, y3), (x4, y4)):
                    intersecting_wires += 1

# Print the number of intersecting wires
print(intersecting_wires)


# Function to check if two wires intersect
def intersect(p1, q1, p2, q2):
    # Find the orientations of the two line segments
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # Check if the line segments intersect
    if (o1 != o2) and (o3 != o4):
        return True
        
    # Special Cases
    # p1, q1 and p2 are collinear and p2 lies on the segment p1q1
    if (o1 == 0) and on_segment(p1, p2, q1):
        return True
         
    # p1, q1 and q2 are collinear and q2 lies on the segment p1q1
    if (o2 == 0) and on_segment(p1, q2, q1):
        return True
 
    # p2, q2 and p1 are collinear and p1 lies on the segment p2q2
    if (o3 == 0) and on_segment(p2, p1, q2):
        return True
 
    # p2, q2 and q1 are collinear and q1 lies on the segment p2q2
    if (o4 == 0) and on_segment(p2, q1, q2):
        return True
 
    return False


# Function to find the orientation of three points
def orientation(p, q, r):
    val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))

    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counter-clockwise


# Function to check if a point lies on a line segment
def on_segment(p, q, r):
    if (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1])):
        return True
 
    return False
