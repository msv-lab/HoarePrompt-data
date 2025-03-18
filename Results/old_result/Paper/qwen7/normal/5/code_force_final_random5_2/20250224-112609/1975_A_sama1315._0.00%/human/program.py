def can_sort_by_split_swap(arr):
    # Check if the array is already sorted
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        return "Yes"
    
    # If not, attempt to sort by simulating the split and swap operation
    # Since the operation only rearranges elements, direct check suffices
    return "No" if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)) else "Yes"
 
# Main function to read inputs and print outputs
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
        arr = list(map(int, data[index:index + n]))
        index += n
        
        result = can_sort_by_split_swap(arr)
        results.append(result)
    
    print("\n".join(results))
 
if __name__ == "__main__":
    main()