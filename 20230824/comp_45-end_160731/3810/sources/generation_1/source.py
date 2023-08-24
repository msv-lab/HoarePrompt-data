def calculate_piles(n, boxes):
    # The idea is to calculate the number of distinct piles 
    # with the maximum number of boxes that ROBO_Head can have.
    # We can iterate from the smallest box to the largest box.
    # For each box, we check if it can be added to any existing pile.
    # If it can be added, then the number of piles with that box
    # as the topmost box is equal to the number of piles ending with
    # a box that divides the current box.
    # If it cannot be added to any existing pile, then the number
    # of new piles with that box as the topmost box is equal to
    # the total number of piles so far.
    
    mod = 10**9 + 7
    
    # Sort the boxes
    sorted_boxes = sorted(boxes)
    
    # Initialize variables
    num_piles = 0
    piles = []
    
    # Iterate from the smallest box to the largest box
    for i in range(n):
        box = sorted_boxes[i]
        
        # Check if the box can be added to any existing pile
        can_be_added = False
        for j in range(num_piles):
            topmost_box = piles[j][-1]
            if box % topmost_box == 0:
                piles[j].append(box)
                can_be_added = True
        
        # If the box cannot be added to any existing pile, create a new pile
        if not can_be_added:
            piles.append([box])
            num_piles += 1
    
    # Calculate the result as the sum of the lengths of all piles
    result = sum(len(pile) for pile in piles)
    
    # Return the result modulo 10^9 + 7
    return result % mod

# Read inputs
n = int(input())
boxes = [int(x) for x in input().split()]

# Calculate the number of distinct piles
num_distinct_piles = calculate_piles(n, boxes)

# Print the result
print(num_distinct_piles)