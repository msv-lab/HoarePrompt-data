#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element.
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
        
    #State: Output State: `empty` is False, `t` is an input integer, `u` and `v` are integers such that 1 ≤ `u`, `v` ≤ `n`, `n` is an integer input from the user, and `tree` is a deque with elements added based on the given conditions. The `tree` deque will contain pairs of integers `(u, v)` or `(v, u)` depending on their positions in the input, with the first element always being `u` and the second element being `v` or vice versa if they match the conditions specified in the loop.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `empty` is False, `t` is an input integer, `u` is `min(t, idx)`, `v` is `min(t, n - idx - 1)`, `n` is an integer input from the user, `tree` is a deque with elements added based on the given conditions, `start` is an input integer, `idx` is the index of `start` in the deque `tree`. If there exists at least one move in `moves` which is odd, then no specific changes are mentioned. If all moves in `moves` are even numbers, then no specific changes are mentioned as well.
#Overall this is what the function does:The function processes a tree structure defined by a series of edges and determines whether a player (Ron or Hermione) wins based on a given number of moves \( t \). It reads the number of nodes \( n \), the number of moves \( t \), and the starting node. The function then builds a deque representing the tree based on the input edges. After identifying the index of the starting node within this deque, it calculates two possible moves and checks if either of them is odd. If at least one move is odd, it prints 'Ron'; otherwise, it prints 'Hermione'.

