#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer and t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the tree described by the edges (u, v) has exactly two leaves. The initial node u_1 is an integer such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: The loop modifies the `lst` dictionary by appending `b` to the list of `a` and `a` to the list of `b` for each iteration. After `x - 1` iterations, `lst` will contain `x` edges, and the lists associated with each node will include all the nodes it is connected to. The values of `n`, `t`, `u`, `v`, `u_1`, and `y` remain unchanged.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: The `lst` dictionary will have all its lists empty, `x` will be the last node that had a non-empty list before the loop ended, `y` will be the last node popped from `lst[x]`, and `s` will be `False`. The values of `n`, `t`, `u`, `v`, and `u_1` remain unchanged.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Hermione
#Overall this is what the function does:The function `func` reads an integer `x` and an integer `y` from the input, constructs a tree represented as a dictionary of lists where each key is a node and each list contains the nodes it is connected to. It then traverses the tree in a specific manner, toggling a boolean variable `s` based on the traversal. Finally, it prints 'Hermione' if `s` is `True` and 'Ron' if `s` is `False`. The function does not return any value. The initial parameters `n`, `t`, `u`, `v`, and `u_1` are not used within the function and remain unchanged.

