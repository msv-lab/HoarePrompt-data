#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) with 1 ≤ u_i ≤ n representing the initial positions of the stone for each round.
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
        
    #State: `n` is an integer read from input such that 2 ≤ n ≤ 2×10^5, `t` is 1, the tree is represented by a deque containing a sequence of node IDs from one leaf to the other leaf of the tree, and `empty` is False.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `n` is an integer read from input such that 2 ≤ n ≤ 2×10^5, `t` is 1, the tree is represented by a deque containing a sequence of node IDs from one leaf to the other leaf of the tree, and `empty` is False; `start` is an integer read from input; `idx` is the index of `start` in `tree`; `moves` is a list containing `[min(1, idx), min(1, n - idx - 1)]`. At least one of the elements in `moves` is odd if the if condition is met, otherwise both elements in `moves` are even numbers.
#Overall this is what the function does:The function reads the number of nodes `n` in a tree, the number of rounds `t` (which is always 1), the edges of the tree, and the initial position of a stone. It determines whether, after moving the stone towards a leaf node for `t` steps, the stone ends up at a position that is an odd distance from one of the leaves. If so, it prints "Ron"; otherwise, it prints "Hermione".

