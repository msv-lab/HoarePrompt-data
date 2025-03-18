#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer such that 1 ≤ u_1 ≤ n.
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
        
    #State: Output State: `empty` is False, `t` remains the same, `u` and `v` are updated based on the last input, `n` remains the same, and `tree` is a deque containing integers after processing all inputs. The `tree` deque will contain the integers `u` and `v` from each input line, depending on their positions relative to the deque's first and last elements, starting with the first two integers added when `empty` is True.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `empty` is False, `t` remains the same, `u` and `v` are equal to `min(t, idx)` and `min(t, n - idx - 1)` respectively, `n` remains the same, `tree` is a deque containing integers after processing all inputs with the integer `start` added to the end, `idx` is the index of `start` in `tree`. If there is at least one odd move in `moves`, then the conditions related to `u` and `v` remain unchanged. If all moves in `moves` are even, then the conditions related to `u` and `v` also remain unchanged.
#Overall this is what the function does:The function processes a tree structure defined by a series of edges and determines whether Ron or Hermione can win a game based on the given conditions. It reads the number of nodes (n), the target move count (t), and the edges of the tree. After constructing the tree, it takes a starting node (start) as input and calculates the minimum moves needed to reach the start node from both ends of the tree. Depending on whether these moves are odd or even, it prints either "Ron" or "Hermione". The function does not return any value but prints the result directly.

