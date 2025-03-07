#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains t integers such that 1 ≤ u_1, ..., u_t ≤ n. The tree is guaranteed to have exactly two leaves.
def func_1():
    n, t = map(int, input().split())
    tree = deque()
    empty = True
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        if empty:
            tree.append(u)
            tree.append(v)
            empty = False
        elif v == tree[0]:
            tree.appendleft(u)
        elif v == tree[-1]:
            tree.append(u)
        elif u == tree[0]:
            tree.appendleft(v)
        elif u == tree[-1]:
            tree.append(v)
        
    #State: Output State: The `tree` deque will contain `n` elements, where `n` is the input integer provided. The `empty` variable will be `False` since the loop has completed all its iterations. The order of elements in `tree` will depend on the inputs provided during each iteration of the loop. Specifically, for each pair `(u, v)`:
    #
    #- If `v` is the first element of `tree`, `u` is added to the beginning of `tree`.
    #- If `v` is the last element of `tree`, `u` is added to the end of `tree`.
    #- Otherwise, `u` is added to the end of `tree` and `v` is added to the end of `tree`.
    #
    #The `i` variable will be `n`, indicating that the loop has executed `n-1` times.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `tree` deque contains `n` elements, `empty` is `False`, `i` is `n`, `idx` is the index of `start` in `tree`, `moves` is a list containing `[min(n, idx), min(n, n - idx - 1)]`. If at least one move in `moves` is odd, the postcondition remains as described in the if part. If all moves in the `moves` list are even numbers, the postcondition remains as described in the else part.
#Overall this is what the function does:The function processes an integer `n` representing the number of nodes in a tree (2 ≤ n ≤ 2 × 10^5), an integer `t` (t = 1), and pairs of integers `u` and `v` representing edges in the tree (1 ≤ u, v ≤ n). It constructs a deque `tree` based on the given edges. After constructing the tree, it finds the index of a specified starting node and calculates the minimum distances to the two leaves of the tree. Depending on whether these distances are odd or even, it prints either "Ron" or "Hermione". The function returns nothing but prints the result based on the calculated conditions.

