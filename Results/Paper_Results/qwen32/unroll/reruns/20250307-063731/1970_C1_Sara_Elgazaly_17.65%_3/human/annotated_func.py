#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer where t=1, the next n-1 lines contain pairs of integers (u, v) representing the edges of the tree (1 ≤ u, v ≤ n), and the last line contains t integers (u_1) representing the starting node of the stone (1 ≤ u_1 ≤ n). The tree is guaranteed to have exactly two leaves.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: `lst` contains the adjacency list for the first `x - 1` edges of the tree; `n`, `t`, `u_1`, `x`, and `y` remain unchanged.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: `lst` with some lists emptied, `x` being the last node processed with an empty list in `lst`, `s` toggled to its final state.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Output:
#Overall this is what the function does:The function determines the winner ('Hermione' or 'Ron') of a game played on a tree structure. The game involves moving a stone from a starting node to a farthest leaf node, and the winner is decided based on the parity of the number of moves required to reach the farthest leaf. The function accepts the number of nodes `n` in the tree, a list of `n-1` edges representing the tree, and a starting node `u_1`. It prints 'Hermione' if the number of moves is odd, otherwise it prints 'Ron'.

