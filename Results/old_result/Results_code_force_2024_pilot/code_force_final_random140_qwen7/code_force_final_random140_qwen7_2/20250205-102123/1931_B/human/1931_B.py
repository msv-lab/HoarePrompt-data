def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Number of containers
        a = list(map(int, input().split()))  # Amount of water in each container
        
        # Calculate total sum of water
        total_water = sum(a)
        
        # The target amount of water each container should have
        target = total_water // n
        
        # Variable to track water deficit/excess during redistribution
        current_balance = 0
        possible = True
        
        # Traverse the containers to check if redistribution is feasible
        for i in range(n):
            current_balance += a[i] - target
            if current_balance < 0:
                possible = False
                break
        
        # Output the result for this test case
        if possible:
            print("YES")
        else:
            print("NO")
 
if __name__ == "__main__":
    main()