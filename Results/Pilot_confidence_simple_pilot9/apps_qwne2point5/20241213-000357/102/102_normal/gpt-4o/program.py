def main():
    # Read input
    n = int(input())
    a = int(input())
    b = int(input())

    # Iterate over possible values of x from 0 to n//a
    for x in range(n // a + 1):
        # Check if the remaining amount can be exactly divided by b
        if (n - x * a) % b == 0:
            y = (n - x * a) // b
            # Print YES and the values of x and y
            print("YES")
            print(x, y)
            return
    
    # If no valid (x, y) pair is found, print NO
    print("NO")

if __name__ == "__main__":
    main()
