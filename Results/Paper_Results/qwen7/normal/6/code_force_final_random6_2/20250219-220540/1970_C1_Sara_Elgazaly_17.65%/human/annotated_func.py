#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer u_1 such that 1 ≤ u_1 ≤ n. The tree is represented by its edges, ensuring there are exactly two leaves.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: Output State: The loop will execute `x-1` times. After all iterations, `x` must be greater than or equal to the total number of iterations, which is `x-1 + 1 = x`. Therefore, `x` can be any integer greater than or equal to 4 (since it must be greater than 3 as per the previous states).
    #
    #- `y` remains an integer input from the user.
    #- `n` is an integer such that \(2 \leq n \leq 2 \times 10^5\).
    #- `t` is 1.
    #- `u` and `v` are integers such that \(1 \leq u, v \leq n\).
    #- The list of integers for the starting node(s) contains exactly one integer \(u_1\) such that \(1 \leq u_1 \leq n\).
    #- `a` and `b` are integers that are inputs to the loop, with `a` being the first integer and `b` being the second integer from each input pair.
    #- `lst` is a defaultdict where all values are lists. After the loop completes, for every pair `(a, b)` that was input, both `lst[a]` and `lst[b]` will contain each other, meaning `a` and `b` are connected nodes in the graph represented by `lst`.
    #
    #In summary, after all iterations of the loop, `lst` will represent an undirected graph with `n` nodes, where each edge connects two nodes based on the pairs provided by the user.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: Output State: `s` is False, `x` is equal to `y`, `y` is the last remaining element in `lst[x]` after all possible pops, `n` is an integer such that \(2 \leq n \leq 2 \times 10^5\), `t` is 1, `u` and `v` are integers such that \(1 \leq u, v \leq n\), the list of integers for the starting node(s) contains exactly one integer \(u_1\) such that \(1 \leq u_1 \leq n\), `a` and `b` are integers that are inputs to the loop, with `a` being the first integer and `b` being the second integer from each input pair, `lst` is a defaultdict where all values are lists, and after all iterations of the loop, `lst[x]` is either empty or contains no elements that can be popped because the loop has terminated.
    #
    #This final state occurs because the loop continues to pop elements from `lst[x]` until it is empty. Once `lst[x]` is empty, the condition `lst[x] != []` becomes false, and the loop terminates. At this point, `s` will be set to `not s`, which means it will be `False` if it was `True` before the last iteration, or `True` if it was `False`. However, since the loop exits when `lst[x]` is empty, `s` will be `False` after the loop completes. Additionally, `x` will be set to `y` just before the loop exits, making `x` equal to `y`.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function constructs an undirected graph representing a tree with \(n\) nodes using input edges. It then traverses the graph starting from the node \(u_1\) and alternates between two states, flipping a boolean flag `s` each time it reaches a leaf node. Finally, it prints either "Hermione" or "Ron" based on the value of `s` after traversal.

