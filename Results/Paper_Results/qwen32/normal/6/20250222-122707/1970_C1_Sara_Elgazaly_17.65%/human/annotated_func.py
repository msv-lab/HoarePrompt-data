#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers u_1, ..., u_t with 1 ≤ u_1, ..., u_t ≤ n, representing the starting node for each round. Since t=1, there is exactly one starting node.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves, the last line contains t integers u_1, ..., u_t with 1 ≤ u_1, ..., u_t ≤ n, representing the starting node for each round, `x` is an integer such that x ≥ 2, `y` is assigned the value of the other integer read from the input, `lst` is a defaultdict of lists where each key (node) has a list of its adjacent nodes representing the entire tree structure.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: `x` is a leaf node, `y` is the last node that was popped from `lst[x]` in the last iteration, `lst[x]` is an empty list, and `s` is `False` if the number of iterations is odd, and `True` if the number of iterations is even.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Hermione if the number of iterations is odd, otherwise Ron
#Overall this is what the function does:The function determines the winner of a game based on traversing a tree structure starting from a given node. It prints 'Hermione' if the number of steps taken to reach a leaf node is odd, otherwise it prints 'Ron'. The tree is guaranteed to have exactly two leaves.

