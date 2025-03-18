#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t=1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) where each u_i is an integer such that 1 ≤ u_i ≤ n, representing the starting node for each round.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1, ..., u_t) where each u_i is an integer such that 1 ≤ u_i ≤ n, representing the starting node for each round. `x` is 2, `y` are the two integers read from the input, `lst` is a defaultdict of lists where for every pair (a, b) read during the iterations, `lst[a]` contains `b` exactly `x - 1` times and `lst[b]` contains `a` exactly `x - 1` times.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: `lst[x]` is empty, `x` is the last node that was fully explored, `y` is the last element that was popped from `lst[x]` in the final iteration, and `s` is False.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Hermione
#Overall this is what the function does:The function reads input representing a tree with exactly two leaves and a starting node. It then performs a traversal process on the tree starting from the given node and determines the winner between 'Hermione' and 'Ron' based on the final state of the traversal. The function outputs the name of the winner.

