def can_sort_letters(s, k):
    # Sort the string in increasing order
    sorted_s = sorted(s)
    
    # Create a list to keep track of the indices where the letters are sorted
    sorted_indices = []
    
    # Check if it is possible to sort the letters
    for i in range(len(s)):
        # Check if the letter is already at the correct position
        if s[i] == sorted_s[i]:
            sorted_indices.append(i)
            continue
        
        # Check if a long swap is possible
        swappable_indices = []
        for j in sorted_indices:
            if abs(i-j) >= k:
                # Swap the letters
                s[i], s[j] = s[j], s[i]
                sorted_indices.append(i)
                swappable_indices.append(i)
                break
        
        # Update sorted_indices with swappable_indices
        sorted_indices.extend(swappable_indices)
    
    # Check if all letters are sorted
    return s == sorted_s

# Read the input string and k value
s, k = input().split()
k = int(k)

# Check if it is possible to sort the letters
if can_sort_letters(list(s), k):
    print("Yes")
else:
    print("No")