#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, t is an integer and t=1, the next n-1 lines contain pairs of integers (u, v) representing edges of the tree where 1 <= u, v <= n, and the tree has exactly two leaves, the last line contains t integers (u_1) representing the starting node of the stone where 1 <= u_1 <= n.
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
        
    #State: `n` is the first integer read from the input, `t` is the second integer read from the input, the next n-1 lines contain pairs of integers (u, v) representing edges of the tree where 1 <= u, v <= n, and the tree has exactly two leaves, the last line contains t integers (u_1) representing the starting node of the stone where 1 <= u_1 <= n, `tree` is a deque containing all n nodes in the correct order from one leaf to the other, `empty` is False.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `n` is the first integer read from the input, `t` is the second integer read from the input, the next n-1 lines contain pairs of integers (u, v) representing edges of the tree where 1 <= u, v <= n, and the tree has exactly two leaves, the last line contains t integers (u_1) representing the starting node of the stone where 1 <= u_1 <= n, `tree` is a deque containing all n nodes in the correct order from one leaf to the other, `empty` is False, `start` is the integer read from the input, `idx` is the index of `start` in `tree`, `moves` is `[min(t, idx), min(t, n - idx - 1)]`. At least one of the values in `moves` is odd, or all elements in `moves` are even numbers.
#Overall this is what the function does:The function reads input representing a tree with `n` nodes and `n-1` edges, ensuring the tree has exactly two leaves. It also reads a starting node `u_1`. Based on the structure of the tree and the starting node, it determines if the stone can be moved to a leaf in an odd number of steps. If so, it prints "Ron"; otherwise, it prints "Hermione".

