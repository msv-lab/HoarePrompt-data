#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, t is an integer equal to 1, the next n-1 lines each contain two integers u and v such that 1 <= u, v <= n representing the edges of the tree, and the last line contains t integers u_1, ..., u_t such that 1 <= u_1, ..., u_t <= n representing the starting nodes for each round.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: `n` is an integer such that 2 <= n <= 2 * 10^5, `t` is an integer equal to 1, the next n-1 lines each contain two integers u and v representing the edges of the tree, and the last line contains t integers u_1, ..., u_t representing the starting nodes for each round; `x` and `y` are the two integers read from the input; `lst` is a defaultdict of lists where each key `a` has a list of integers `b` that were paired with `a` as read from the input for `x - 1` iterations; `rev` is a defaultdict of lists where each key `b` has a list of integers `a` that were paired with `b` as read from the input for `x - 1` iterations.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: Output State: tmp is the last element popped from lst[tmp], and one is True if the number of elements in lst[tmp] is even, otherwise one is False.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: `tmp` is the last element popped from `rev[tmp]` before it becomes empty, `one` remains the same, and `two` is `True` if the number of iterations is even, and `False` if the number of iterations is odd.
    print('Hermione' if two and one else 'Ron')
    #This is printed: 'Hermione' if `two` is `True` and `one` is `True`; otherwise, 'Ron'
#Overall this is what the function does:The function reads the description of a tree with `n` nodes and `n-1` edges, and a starting node. It then determines the final node reached by traversing the tree in two different directions (forward and reverse) from the starting node, and prints 'Hermione' if both traversals result in an even number of steps, otherwise it prints 'Ron'.

