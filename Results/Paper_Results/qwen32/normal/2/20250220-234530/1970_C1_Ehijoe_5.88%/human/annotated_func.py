#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer equal to 1, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n, and the tree has exactly two leaves. There is a single integer u_1 (1 ≤ u_1 ≤ n) representing the initial node where the stone is placed.
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
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `t` is the second integer read from the input, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n, and the tree has exactly two leaves, `u_1` is an integer (1 ≤ u_1 ≤ n), `tree` is a deque representing the entire path of the tree from one leaf to the other, and `empty` is False.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `t` is the second integer read from the input, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n, and the tree has exactly two leaves, `u_1` is an integer (1 ≤ u_1 ≤ n), `tree` is a deque representing the entire path of the tree from one leaf to the other, `empty` is False, `start` is an integer read from the input, `idx` is the index of `start` in `tree`, `moves` is a list `[min(t, idx), min(t, n - idx - 1)]`. At least one of the elements in `moves` is odd, or both elements in `moves` are even numbers.
#Overall this is what the function does:The function reads input values representing a tree with exactly two leaves and an initial node where a stone is placed. It determines whether, starting from the initial node, a player named Ron can make a move that results in an odd number of moves, or if Hermione can ensure that all possible moves result in an even number of moves. The function prints "Ron" if Ron can make such a move, otherwise it prints "Hermione".

