#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer u_1 such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: x is an integer input from the first split, y is an integer input from the second split, n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer u_1 such that 1 ≤ u_1 ≤ n; `lst` is a defaultdict where each key (node) has a list of its adjacent nodes. The list `lst` is populated with edges provided by the input during the loop iterations.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: The variable `s` will be False, and the variables `x`, `y`, `t`, `u`, `v`, and `lst` will retain their original values or states as they were not altered by the loop.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: 'Hermione'
#Overall this is what the function does:The function reads two integers from input, constructs an undirected graph using adjacency lists, and then traverses the graph to determine if a certain condition is met. If the traversal ends without visiting any more nodes, it prints 'Hermione'; otherwise, it prints 'Ron'. The function does not accept any parameters and returns nothing.

