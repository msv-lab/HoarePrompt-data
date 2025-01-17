def count_Pairs(lst, n):
    # Initialize the count
    count = 0
    
    # Iterate through the list using two pointers to form pairs
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] != lst[j]:
                count += 1
    
    return count

# Test cases to validate the solution
assert count_Pairs([1,2,1],3) == 2
assert count_Pairs([1,1,1,1],4) == 0
assert count_Pairs([1,2,3,4,5],5) == 10
