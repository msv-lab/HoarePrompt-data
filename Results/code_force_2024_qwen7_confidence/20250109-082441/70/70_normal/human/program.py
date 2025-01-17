def count_beautiful_pairs(arr):
    # Sort the array to group similar values together
    arr.sort()
    
    # Initialize counters for beautiful pairs
    cnt = 0
    
    # Iterate over the array to find beautiful pairs
    for i in range(len(arr) - 2):
        current = arr[i]
        next_next = arr[i + 1]
        
        # Check all combinations of 'current', 'next_next', and 'next_next' for beauty
        # Adjust counts for double occurrences from sort order
        if current != next_next and current != arr[i + 2]:
            cnt += 1
            
            # Special handling for perfect matches
            if current == arr[i + 1] == arr[i + 2]:
                cnt -= 1
                
    return cnt // 2  # Divide by 2 because every valid pair has been counted twice

# Main function to handle multiple test cases
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        result = count_beautiful_pairs(arr)
        results.append(result)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()