#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, and the tree is represented by a list of n-1 edges where each edge is a tuple (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The starting node u_1 is an integer such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: The loop has modified the `lst` dictionary by appending `x - 1` pairs of integers (a, b) to the corresponding lists. The variables `n`, `u_1`, `x`, and `y` remain unchanged.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: The `lst` dictionary remains with the same keys but all lists are empty. The variable `s` is `False`. The variables `n`, `u_1`, `x`, and `y` are unchanged.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Hermione
#Overall this is what the function does:The function reads an integer `x` and an integer `y` from the input, then reads `x - 1` pairs of integers representing edges of a tree. It processes the tree to determine the other leaf node starting from node `x`. The function prints 'Hermione' if the other leaf node is reached after an even number of steps, and 'Ron' if it is reached after an odd number of steps. The function does not return any value.

