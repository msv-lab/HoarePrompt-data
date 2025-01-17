import sys

def solve():
    inp = sys.stdin.readline
    n = int(inp())
    # Initialize a list to store arm intervals for each player
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        # Read and store the arm interval for each player
        a[i] = list(map(int, inp().split()))
    
    # Sort the arm intervals based on the starting point
    a.sort()
    
    # Initialize the answer with 1, as at least one round is needed
    ans = 1
    for i in range(1, n):
        # If the current start is greater than the previous end, increment the round count
        if a[i][0] > a[i - 1][1]:
            ans += 1
        # Update the maximum end point
        a[i - 1][1] = max(a[i - 1][1], a[i][0] - 1)
    
    # Print the result for the current test case
    print(ans)

def main():
    # Read the number of test cases
    for _ in range(int(sys.stdin.readline())):
        solve()

if __name__ == '__main__':
    main()