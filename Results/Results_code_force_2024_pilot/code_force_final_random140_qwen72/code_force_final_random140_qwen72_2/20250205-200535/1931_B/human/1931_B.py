def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Read the value of n
        arr = list(map(int, input().split()))  # Read the array
        arr.sort()  # Sort the array
        # Example: check if array is increasing
        if all(arr[i] <= arr[i+1] for i in range(n-1)):
            print("YES")
        else:
            print("NO")
 
if __name__ == "__main__":
    main()