#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t=1, the tree has exactly n nodes and n-1 edges, the tree has exactly two leaves, and the next line contains t integers (in this case, a single integer) 1 ≤ u_1 ≤ n, representing the starting node for the round.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is an integer such that t=1, the tree has exactly n nodes and n-1 edges, the tree has exactly two leaves, and the next line contains t integers (in this case, a single integer) 1 ≤ u_1 ≤ n, representing the starting node for the round; `x` and `y` are the two integers read from the input; `lst` is a defaultdict of lists representing the adjacency list of the tree; `rev` is a defaultdict of lists representing the reverse adjacency list of the tree.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: one is True, tmp is 1.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: one is True, tmp is z, two is True.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Hermione
#Overall this is what the function does:The function reads input representing a tree with `n` nodes and `n-1` edges, having exactly two leaves. It also reads a starting node `u_1`. The function then determines, based on the structure of the tree and the starting node, whether to print "Hermione" or "Ron".

