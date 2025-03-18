#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer equal to 1, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) where each u_i is an integer such that 1 ≤ u_i ≤ n, representing the starting node for each round.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is an integer equal to 1, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) where each u_i is an integer such that 1 ≤ u_i ≤ n, representing the starting node for each round. `x` is an integer such that x ≥ 1, `y` is an integer, `lst` is a defaultdict of lists with `lst[a]` now including `b` for all edges (a, b) read from the input, and `rev` is a defaultdict of lists where `rev[b]` includes `a` for all edges (a, b) read from the input.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is an integer equal to 1, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) where each u_i is an integer such that 1 ≤ u_i ≤ n, representing the starting node for each round. `x` is an integer such that x ≥ 1, `y` is an integer, `lst` is a defaultdict of lists with `lst[a]` now including `b` for all edges (a, b) read from the input except all edges leading to the leaf node `tmp` have been removed, `rev` is a defaultdict of lists where `rev[b]` includes `a` for all edges (a, b) read from the input, `z` is an integer such that `z` is a node in the tree and there is at least one edge connected to `z`, `tmp` is a leaf node of the tree, `one` is either True or False depending on the number of iterations.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is an integer equal to 1, the tree is represented by n-1 edges given as pairs of integers (u, v) where 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) where each u_i is an integer such that 1 ≤ u_i ≤ n, representing the starting node for each round. `x` is an integer such that x ≥ 1, `y` is an integer, `lst` is a defaultdict of lists with `lst[a]` now including `b` for all edges (a, b) read from the input except all edges leading to the leaf node `tmp` have been removed, `rev` is a defaultdict of lists where `rev[b]` includes `a` for all edges (a, b) read from the input except the edges leading to `tmp` have been removed, `z` is an integer such that `z` is a node in the tree and there is at least one edge connected to `z`, `tmp` is a leaf node, `one` is either True or False depending on the number of iterations, `two` is True if the number of iterations is even, and False if the number of iterations is odd, and `rev[tmp]` is an empty list.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Hermione if `two` and `one` are both True, otherwise Ron
#Overall this is what the function does:The function reads the description of a tree with exactly two leaves and a starting node. It then determines and prints 'Hermione' if the path from the starting node to one leaf and back to the other leaf involves an even number of steps, otherwise it prints 'Ron'.

