def solve():
    t = int(input())  # Number of test cases
    
    for _ in range(t):
        n = int(input())  # Number of books
        a = list(map(int, input().split()))  # List of pages in each book
        
        # Sort the list in descending order
        a.sort(reverse=True)
        
        # Check if the two largest values are the same
        max1 = a[0]
        max2 = a[1]
        
        # If the two largest values are the same, we need to look for the next largest distinct value
        if max1 == max2:
            for i in range(2, n):
                if a[i] != max1:
                    max2 = a[i]
                    break
        
        # Output the sum of the two largest distinct values
        print(max1 + max2)

# Run the solution
solve()