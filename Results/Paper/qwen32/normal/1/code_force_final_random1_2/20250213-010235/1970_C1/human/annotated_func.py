#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer equal to 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) with 1 ≤ u_i ≤ n representing the starting node for each round.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2 × 10^5, `t` is an integer equal to 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves, the last line contains t integers (u_1, ..., u_t) with 1 ≤ u_i ≤ n representing the starting node for each round, `x` is an integer read from the input, `y` is an integer read from the input, `lst` is a defaultdict with list as the default factory and `lst[a]` now includes all `b` values corresponding to the edges read during the loop, `rev` is a defaultdict with list as the default factory and `rev[b]` now includes all `a` values corresponding to the edges read during the loop, `a` and `b` are integers read from the input.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: `tmp` is a leaf node of the tree, and `lst[tmp]` is an empty list.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: `tmp` is the last element popped from the deepest non-empty list in `rev`; `two` is `False` if the number of iterations is odd, or `True` if the number of iterations is even; `rev[tmp]` is an empty list.
    print('Hermione' if two and one else 'Ron')
    #This is printed: 'Ron' if `two` is `False`, otherwise 'Hermione' if `two` is `True` and `one` is `True`
#Overall this is what the function does:The function determines the winner between 'Hermione' and 'Ron' based on traversing a tree structure starting from a given node. It reads the number of nodes, the tree edges, and a starting node, then performs two separate traversals from the starting node to determine the final state, which dictates the winner.

