#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, the next n-1 lines contain pairs of integers (u, v) representing edges of the tree where 1 ≤ u, v ≤ n, and the tree has exactly two leaves, and the last line contains t integers (u_1, ..., u_t) representing the starting nodes for the stone where 1 ≤ u_1, ..., u_t ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: `lst` is a defaultdict of lists representing the adjacency list of the tree, and `rev` is a defaultdict of lists representing the reverse adjacency list of the tree. All other variables remain unchanged.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: `tmp` is the last node visited, `lst[tmp]` is an empty list, and `one` is either `True` or `False` depending on the number of iterations.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: `tmp` is `z`, `two` is `True`, `one` is unchanged, `lst[z]` is an empty list.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Hermione if one is True, otherwise Ron
#Overall this is what the function does:The function determines the winner of a game played on a tree structure. Given a tree with `n` nodes and `n-1` edges, and a starting node for a stone, the function computes whether 'Hermione' or 'Ron' wins based on the parity of the paths from the starting node to the leaves of the tree.

