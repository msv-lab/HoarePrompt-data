#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains t integers such that 1 ≤ u_1, ..., u_t ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: `a` is an integer equal to the first input number; `b` is an integer equal to the second input number; `lst[a]` and `lst[b]` both contain a list of integers representing all the nodes connected to `a` and `b` respectively through the edges defined by the inputs during each iteration of the loop; `x` must be greater than 2×10^5 since the loop runs `x-1` times and `2 ≤ n ≤ 2×10^5`.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: Output State: `s` is `True`, `a` is an integer equal to the first input number, `b` is an integer equal to the second input number, `lst[a]` remains unchanged, `x` is set to the last element that was popped from `lst[x]` during the last iteration of the loop, and `lst[x]` is an empty list. The variable `lst[y]` corresponding to the value of `x` is non-empty, where `y` is the value that was popped from `lst[x]` in the previous iteration.
    #
    #This means that after all iterations of the loop have finished, the variable `s` will be `True` because it toggles between `True` and `False` with each iteration, and since the loop terminates when `lst[x]` becomes an empty list, `s` will end up as `True`. The variable `x` will be set to the last node that was popped from `lst[x]` before the list became empty. All other variables (`a`, `b`, `lst[a]`, and `lst[b]`) remain unchanged from their initial or previous states.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function reads two integers from input, constructs an undirected graph using adjacency lists, and then traverses the graph starting from the first integer. It alternates between two states (True and False) until it reaches a leaf node (a node with no outgoing edges). Finally, it prints 'Ron' if the last state is True, otherwise it prints 'Hermione'. The function does not accept any parameters and relies on external input constraints.

