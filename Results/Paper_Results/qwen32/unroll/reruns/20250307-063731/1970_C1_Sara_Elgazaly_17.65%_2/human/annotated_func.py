#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t=1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers 1 ≤ u_1, ..., u_t ≤ n, representing the starting node for each round.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: - After the loop finishes, `lst` will contain the adjacency list representation of the tree constructed from the `x - 1` edges provided in the input.
    #   - The values of `n`, `t`, the starting node, and `y` remain unchanged as they are not affected by the loop.
    #   - The tree structure will be fully represented in `lst` after the loop completes.
    #
    #Given this analysis, the output state can be described as follows:
    #
    #Output State:
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: The loop will terminate when all nodes connected to the starting node have been visited and their neighbors have been processed. The final value of `x` will be a node that has no unvisited neighbors, and `s` will be `True` if the number of iterations is even, or `False` if the number of iterations is odd.
    #
    #Output State:
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Hermione if the number of iterations is odd, Ron if the number of iterations is even
#Overall this is what the function does:The function determines whether the number of iterations required to traverse a tree from a given starting node is odd or even. It prints "Hermione" if the number of iterations is odd and "Ron" if the number of iterations is even. The tree is represented by a list of edges, and the starting node is provided as input.

