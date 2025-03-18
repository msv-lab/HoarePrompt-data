#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, representing the number of nodes in the tree. The tree is represented by n-1 edges, each connecting two nodes u and v where 1 ≤ u, v ≤ n, and it is guaranteed that the tree has exactly two leaves. The initial position of the stone is given by an integer u_1 where 1 ≤ u_1 ≤ n.
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
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `t` is an input integer, `u_1` is an integer where 1 ≤ u_1 ≤ n, `i` is `n-2`, `u` and `v` are integers provided by user input, `empty` is False, and `tree` is a deque containing a sequence of integers representing the nodes of a tree structure, with the first and last elements being the endpoints of the longest path in the tree.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *`n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `t` is an input integer, `u_1` is an integer where 1 ≤ u_1 ≤ n, `i` is `n-2`, `u` and `v` are integers provided by user input, `empty` is False, `tree` is a deque containing a sequence of integers representing the nodes of a tree structure, with the first and last elements being the endpoints of the longest path in the tree, `start` is an input integer, `idx` is the index of `start` in `tree`, `moves` is a list containing `[min(t, idx), min(t, n - idx - 1)]`. If at least one element in `moves` is odd, the program follows the logic for the if part. Otherwise, all elements in `moves` are even, and the program follows the logic for the else part.
#Overall this is what the function does:The function reads inputs to construct a tree representation using a deque, where the tree is defined by `n` nodes and `n-1` edges. It then determines the starting position of a stone on the tree and calculates the minimum number of moves required to move the stone to one of the two leaves of the tree. Based on the parity (odd or even) of these moves, it prints either 'Ron' or 'Hermione'. The function does not return any value; it only prints the result based on the game's rules.

