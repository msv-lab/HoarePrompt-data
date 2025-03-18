def can_sort_by_swapping(a):
    n = len(a)
    sorted_a = sorted(a)
    concatenated_a = a + a
    
    # Check if sorted_a is a subarray of concatenated_a
    for i in range(n):
        if concatenated_a[i:i+len(sorted_a)] == sorted_a:
            return "Yes"
    return "No"
 
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        result = can_sort_by_swapping(a)
        results.append(result)
    print("\n".join(results))
 
if __name__ == "__main__":
    main()