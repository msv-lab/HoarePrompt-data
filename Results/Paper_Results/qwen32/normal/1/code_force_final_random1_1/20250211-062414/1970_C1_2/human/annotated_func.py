#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer equal to 1, the next n-1 lines each contain two integers u and v representing edges of the tree, and the last line contains a single integer u_1 representing the initial node where the stone is placed. The tree is guaranteed to have exactly two leaves.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is an integer equal to 1, the next n-1 lines each contain two integers u and v representing edges of the tree, the last line contains a single integer u_1 representing the initial node where the stone is placed, `x` is an integer, `y` is an integer, `lst` is a defaultdict with list as the default factory containing x-1 mappings from node a to lists of nodes b, and `rev` is a defaultdict with list as the default factory containing x-1 mappings from node b to lists of nodes a.`
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5; `t` is an integer equal to 1; the next n-1 lines each contain two integers u and v representing edges of the tree; the last line contains a single integer u_1 representing the initial node where the stone is placed; `x` is an integer; `y` is an integer; `lst` is a defaultdict with list as the default factory containing x-1 mappings from node a to lists of nodes b, and `lst[tmp]` is now empty; `rev` is a defaultdict with list as the default factory containing x-1 mappings from node b to lists of nodes a; `z` is an input integer; `tmp` is the last node from which an element was popped; `one` is True if the number of iterations is even, or False if the number of iterations is odd.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: `tmp` is a node with no incoming edges in `rev`; `two` is `False` if the number of iterations is odd, and `True` if the number of iterations is even; all other variables remain unchanged.
    print('Hermione' if two and one else 'Ron')
    #This is printed: 'Hermione' if `two` is `True` and `one` is `True`; otherwise, 'Ron'
#Overall this is what the function does:The function determines the final resting position of a stone on a tree structure after it rolls from an initial node. Given a tree with exactly two leaves, the stone rolls down the tree following the edges until it reaches a leaf node. The function outputs "Hermione" if the stone ends up at one specific leaf and "Ron" if it ends up at the other leaf.

