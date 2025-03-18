#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t=1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) with 1 ≤ u_i ≤ n, representing the starting node for each round.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is an integer such that t=1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) with 1 ≤ u_i ≤ n, representing the starting node for each round. `x` is an integer greater than 1, `y` is an integer read from the input, `lst` is a defaultdict with list as the default value and `lst[b]` now includes `a` along with its previous values for all `x-1` iterations, and `_` is incremented to `x-1`. `a` and `b` are integers read from the input for each iteration.`
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: `lst[x]` is empty, `y` is the last element popped from `lst[x]`, `x` is a leaf node, and `s` is `True` if the number of iterations is even, otherwise `False`.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: The print statement will output either 'Hermione' or 'Ron' based on the value of `s`. Since the exact value of `s` is not provided, we describe it in terms of the condition given.
    #
    #Output:
#Overall this is what the function does:The function reads the description of a tree with `n` nodes and `n-1` edges, where the tree has exactly two leaves, and a starting node. It then determines the winner of a game based on the starting node and the structure of the tree, printing either 'Hermione' or 'Ron'.

