#State of the program right berfore the function call: The function `func_1` does not take any parameters, but it is expected to read input from stdin. The input consists of: the first line containing two integers n (2 ≤ n ≤ 2×10^5) and t (t=1), the number of nodes in the tree and the number of rounds, respectively. The next n-1 lines each contain two integers u and v (1 ≤ u, v ≤ n) representing an edge between nodes u and v in the tree. It is guaranteed that the tree has exactly two leaves. The next line contains t integers (1 ≤ u_1, ..., u_t ≤ n) corresponding to the node where the stone is initially placed for the round.
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
        
    #State: `n` is an integer between 2 and 2×10^5, `t` is 1, `tree` is a deque containing a sequence of integers that form a path in the input graph, `empty` is False.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *`n` is an integer between 2 and 2×10^5, `t` is 1, `tree` is a deque containing a sequence of integers that form a path in the input graph, `empty` is False, `start` is an input integer, `idx` is the index of `start` in `tree`, `moves` is a list containing two elements: the first element is the minimum of `t` and `idx`, and the second element is the minimum of `t` and `n - idx - 1`. If at least one of the elements in `moves` is an odd number, then the program follows the if part. Otherwise, both elements in `moves` are even, and the program follows the else part.
#Overall this is what the function does:The function `func_1` reads input from stdin to construct a tree represented as a deque. It then determines the initial position of a stone on one of the nodes and calculates the minimum number of moves the stone can make to either end of the tree. The function prints 'Ron' if at least one of these minimum moves is an odd number, and 'Hermione' otherwise. The function does not return any value. After the function concludes, the tree is represented as a deque containing a sequence of integers that form a path in the input graph, and the initial node position and calculated moves are no longer relevant.

