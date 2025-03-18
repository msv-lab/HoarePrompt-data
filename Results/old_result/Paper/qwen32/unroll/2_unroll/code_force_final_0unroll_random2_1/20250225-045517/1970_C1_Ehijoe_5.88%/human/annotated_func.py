#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t=1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) with 1 ≤ u_i ≤ n, representing the starting node for each round.
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
        
    #State: `tree` is a deque containing all `n` nodes in a single path from one leaf to the other, `empty` is False.
    start = int(input())
    idx = tree.index(start)
    moves = [min(t, idx), min(t, n - idx - 1)]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `tree` is a deque containing all `n` nodes in a single path from one leaf to the other, `empty` is False, `start` is an input integer, `idx` is the index of `start` in `tree`, `moves` is a list of minimum values between `t` and the distances from `idx` to both ends of `tree`. At least one value in `moves` is odd, or all elements in `moves` are even numbers.
#Overall this is what the function does:The function reads input values representing a tree with exactly two leaves and a starting node. It determines whether a player named Ron or Hermione wins a game based on the minimum number of moves required to reach either leaf from the starting node. The game rules state that if the minimum number of moves to either leaf is odd, Ron wins; otherwise, Hermione wins. The function prints the name of the winning player.

