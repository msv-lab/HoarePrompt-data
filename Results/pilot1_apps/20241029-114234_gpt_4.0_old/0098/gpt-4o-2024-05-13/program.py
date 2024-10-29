def can_place_paintings(a1, b1, a2, b2, a3, b3):
    # Check all possible orientations of the paintings
    possible_orientations = [
        (a2, b2, a3, b3),
        (a2, b2, b3, a3),
        (b2, a2, a3, b3),
        (b2, a2, b3, a3)
    ]
    
    for (w2, h2, w3, h3) in possible_orientations:
        # Check if the paintings can fit side by side or one on top of the other
        if (w2 + w3 <= a1 and max(h2, h3) <= b1) or (max(w2, w3) <= a1 and h2 + h3 <= b1):
            return "YES"
        if (h2 + h3 <= b1 and max(w2, w3) <= a1) or (max(h2, h3) <= b1 and w2 + w3 <= a1):
            return "YES"
    
    return "NO"

# Read input
import sys
input = sys.stdin.read
data = input().split()
a1, b1 = int(data[0]), int(data[1])
a2, b2 = int(data[2]), int(data[3])
a3, b3 = int(data[4]), int(data[5])

# Output the result
print(can_place_paintings(a1, b1, a2, b2, a3, b3))
