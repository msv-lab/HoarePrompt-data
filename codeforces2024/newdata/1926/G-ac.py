for _ in range(int(input())):
    n = int(input())
    # Read the parent array, with a dummy -1 at the start for 1-based indexing
    fa = [-1] + list(map(int, input().split()))
    # Read the string representing student types
    S = input()
    
    # Initialize dp arrays for isolation and non-isolation scenarios
    dp1, dp2 = [0] * (n + 1), [0] * (n + 1)
    
    # Traverse the tree from the last node to the first (bottom-up)
    for i in range(n - 1, -1, -1):
        if S[i] == "S":
            dp1[i] = float("inf")  # Must isolate sleepy students
        elif S[i] == "P":
            dp2[i] = float("inf")  # Must not allow music to pass through partying students

        # Get the parent of the current node
        p = fa[i] - 1
        if p != -1:
            # Update the parent's dp values based on the current node's values
            dp1[p] += min(dp1[i], dp2[i] + 1)
            dp2[p] += min(dp1[i] + 1, dp2[i])

    # Output the minimum number of thick walls needed for the root
    print(min(dp1[0], dp2[0]))