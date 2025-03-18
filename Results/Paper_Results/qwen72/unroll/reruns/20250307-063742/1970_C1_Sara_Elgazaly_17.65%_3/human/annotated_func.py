#State of the program right berfore the function call: The function `func` does not take any parameters, but it is implied that the input is provided externally and consists of a tree with n nodes (2 ≤ n ≤ 2×10^5) and exactly two leaves, and a single round (t=1) where the stone is initially placed on a node (1 ≤ u_1 ≤ n).
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        lst[b].append(a)
        
    #State: After the loop executes all the iterations, `lst` will contain a dictionary where each key is a node in the tree, and the value is a list of nodes that are connected to the key node. The lists will have the neighbors of each node as specified by the input pairs (a, b). The variables `x` and `y` will remain unchanged.
    s = True
    while lst[x] != []:
        while lst[x]:
            y = lst[x].pop()
            if lst[y] != []:
                x = y
                break
        
        s = not s
        
    #State: `lst` is `{1: [], 2: [], 3: [], 4: []}`, `x` is `2`, `y` is `1`, and `s` is `True`.
    s = not s
    print('Hermione' if s else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function `func` reads input describing a tree with `n` nodes (2 ≤ n ≤ 2×10^5) and exactly two leaves, and a starting node for a stone (1 ≤ u_1 ≤ n). It then simulates a process where the stone moves between nodes based on the tree's structure. The function does not return any value but prints either 'Hermione' or 'Ron' based on the final position of the stone after the process completes. The final state of the program is that the tree structure is modified (specifically, the adjacency lists are emptied), and the stone's position is determined, leading to the print statement.

