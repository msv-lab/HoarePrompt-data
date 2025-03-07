#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer such that 1 ≤ u_1 ≤ n.
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
        
    #State: Output State: `empty` is False, `t` remains the same input integer, `u` and `v` are integers that were processed during the loop, `n` remains an integer such that 2 ≤ `n` ≤ 2 × 10^5, and `tree` is a deque containing integers `u` and `v` from the input, with their positions determined by the conditions in the loop.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `empty` is False, `t` remains the same input integer, `u` and `v` are integers that were processed during the loop, `n` remains an integer such that 2 ≤ `n` ≤ 2 × 10^5, `tree` is a deque containing integers `u` and `v` from the input, `idx` is the index of `start` in `tree`, `moves` is a list containing two elements, each element being the minimum of `t` and either `idx` or `n - idx - 1`. At least one of the moves in `moves` is an odd number if the condition `any([move % 2 == 1 for move in moves])` is true, otherwise all elements in `moves` are even.
#Overall this is what the function does:The function processes a tree structure defined by a series of edges and determines whether Ron or Hermione can win a game based on the given conditions. It reads the number of nodes (n), the target move count (t), and the edges of the tree. It then finds a starting node and calculates the minimum moves required to reach the start node from both ends of the tree. If at least one of these minimum moves is odd, it prints 'Ron'; otherwise, it prints 'Hermione'.

