#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element. The tree is represented by its edges, ensuring it has exactly two leaves.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: x is an integer obtained from the first input, y is an integer obtained from the second input, n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) has exactly one element; `lst` is a defaultdict where the default factory is list containing pairs of integers representing bidirectional edges between nodes.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: The variable `s` will be flipped from its initial state (True to False or False to True), and all elements in the list `lst[x]` will be emptied.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: 'Ron' if s is False, otherwise 'Hermione'
#Overall this is what the function does:The function processes a tree structure defined by its edges and two specific nodes \(u\) and \(v\). It checks whether the two nodes are leaves (i.e., nodes with only one edge) and ensures the tree has exactly two leaves. If the condition is met, it prints 'Hermione'; otherwise, it prints 'Ron'.

