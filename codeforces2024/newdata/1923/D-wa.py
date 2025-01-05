import bisect

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Create a prefix sum array
    pref = [arr[i] for i in range(n)]
    for i in range(1, n):
        pref[i] += pref[i-1]
    
    # Initialize the index and answer array
    ind = -1
    ans = [10**9 for i in range(n)]
    
    # Left to right pass
    for i in range(n):
        # Calculate the current value to check against prefix sums
        curr = pref[i] - 2 * arr[i]
        ind1 = bisect.bisect_left(pref, curr)
        
        # Update the minimum index
        ind = min(ind, ind1)
        
        # Check if the current slime can be eaten
        if ind >= 0 and curr > 0:
            ans[i] = (i - ind)
        
        # Check if the current slime can be eaten by the previous one
        if i - 1 >= 0 and arr[i] != arr[i-1]:
            if arr[i] < arr[i-1]:
                ans[i] = 1
                ind = i
    
    # Right to left pass
    ind = n
    for i in range(n-1, -1, -1):
        # Calculate the current value to check against prefix sums
        curr = pref[i] + arr[i] + 1
        ind1 = bisect.bisect_left(pref, curr)
        
        # Update the maximum index
        ind = max(ind, ind1)
        
        # Check if the current slime can be eaten
        if ind < n and curr <= pref[-1]:
            ans[i] = min(ans[i], (ind - i))
        
        # Check if the current slime can be eaten by the next one
        if i + 1 < n and arr[i] != arr[i+1]:
            if arr[i] < arr[i+1]:
                ans[i] = 1
                ind = i
    
    # Replace large numbers with -1 to indicate impossibility
    for i in range(n):
        if ans[i] == 10**9:
            ans[i] = -1
    
    # Print the result for the current test case
    print(*ans)

# Read the number of test cases
for _ in range(int(input())):
    solve()