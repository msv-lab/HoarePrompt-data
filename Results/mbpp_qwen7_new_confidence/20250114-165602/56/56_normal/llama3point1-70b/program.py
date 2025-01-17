def eulerian_num(n, m):
    """
    Calculate the Eulerian number a(n, m)
    
    The Eulerian number a(n, m) counts the number of permutations of n elements
    with exactly m runs of consecutive elements in increasing order.
    
    The formula used here is based on the recursive relationship:
    a(n, m) = (n-m+1) * a(n-1, m-1) + m * a(n-1, m)
    
    :param n: The number of elements
    :param m: The number of runs
    :return: The Eulerian number a(n, m)
    """
    # Base cases
    if m == 0:
        return 0
    if n == m:
        return 1
    
    # Initialize a dictionary to store the results of subproblems
    memo = {(i, j): 0 for i in range(n+1) for j in range(m+1)}
    
    # Base cases
    for i in range(n+1):
        memo[(i, 0)] = 0
        memo[(i, i)] = 1
    
    # Fill the memo dictionary using the recursive relationship
    for i in range(1, n+1):
        for j in range(1, min(i, m)+1):
            memo[(i, j)] = (i-j+1) * memo[(i-1, j-1)] + j * memo[(i-1, j)]
    
    return memo[(n, m)]
