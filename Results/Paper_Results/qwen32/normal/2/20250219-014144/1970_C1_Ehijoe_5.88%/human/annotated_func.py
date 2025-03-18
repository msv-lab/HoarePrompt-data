#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer equal to 1, the tree described by the edges has exactly two leaves, and the edges are provided as pairs of integers (u, v) where 1 ≤ u, v ≤ n. Additionally, there is a single integer u_1 (1 ≤ u_1 ≤ n) representing the initial node where the stone is placed.
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
        
    #State: `tree` is a deque containing all nodes in the order forming a path from one leaf to the other leaf of the tree, and `empty` is `False`.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `tree` is a deque containing all nodes in the order forming a path from one leaf to the other leaf of the tree, `empty` is `False`, `start` is an input integer, `idx` is the index of `start` in `tree`, `moves` is `[min(t, idx), min(t, n - idx - 1)]`. At least one of the elements in `moves` is odd if the if condition is met; otherwise, all elements in `moves` are even numbers.
#Overall this is what the function does:The function determines whether a player named Ron or Hermione wins a game based on the position of a stone on a path in a tree. It accepts the number of nodes `n`, a constant `t` which is always 1, a list of edges forming a path between two leaves in the tree, and the starting node `u_1` where the stone is placed. The function prints 'Ron' if the stone can be moved to another leaf in an odd number of steps, otherwise it prints 'Hermione'.

