def check(arr, fav, k):
    sortedArr = sorted(arr, reverse=True)
    favIndexBeforeSort = arr.index(fav) + 1
    del sortedArr[:k]
    
    if fav in sortedArr:
        favIndexAfterSort = sortedArr.index(fav) + 1
        
        # Check if the favorite cube moved to the left
        if favIndexAfterSort > favIndexBeforeSort:
            return "YES"
        elif favIndexAfterSort == favIndexBeforeSort:
            return "MAYBE"
        else:
            return "NO"
    else:
        return "YES"

# Test cases
print(check([4, 3, 3, 2, 3], 2, 2))  # MAYBE
print(check([4, 2, 1, 3, 5], 5, 3))  # YES
print(check([5, 2, 4, 1, 3], 5, 2))  # NO