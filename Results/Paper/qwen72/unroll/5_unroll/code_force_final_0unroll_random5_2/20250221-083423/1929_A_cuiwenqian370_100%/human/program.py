def max_beauty(array):
    # Sort the array to maximize the absolute differences between consecutive elements
    array.sort()
    # Calculate the maximum beauty by summing the differences between consecutive sorted elements
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i-1])
    return beauty
 
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])  # Number of test cases
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])  # Length of the array
        index += 1
        array = list(map(int, data[index:index+n]))
        index += n
        
        # Calculate the maximum beauty for this array
        result = max_beauty(array)
        results.append(result)
    
    for result in results:
        print(result)
 
if __name__ == "__main__":
    main()