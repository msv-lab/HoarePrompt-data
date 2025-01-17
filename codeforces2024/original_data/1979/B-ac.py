t = int(input())  # Read number of test cases
for _ in range(t):
    a, b = map(int, input().split())  # Read a and b for each test case
    for i in range(30):
        # Check if the ith bit of a and b are different
        if (a & (1 << i)) != (b & (1 << i)):
            print(1 << i)  # Print the result (1 shifted left i times)
            break


