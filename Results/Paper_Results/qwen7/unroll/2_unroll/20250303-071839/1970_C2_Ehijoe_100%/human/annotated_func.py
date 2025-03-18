#State of the program right berfore the function call: nodes is a dictionary representing the tree structure where keys are node indices and values are lists of neighboring nodes; start is an integer representing the starting node index where the stone is initially placed; parent is an optional integer representing the parent node of the current node being processed, defaulting to None.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return False
        #The program returns False
    #State: nodes is a dictionary representing the tree structure where keys are node indices and values are lists of neighboring nodes; start is an integer representing the starting node index where the stone is initially placed; parent is an optional integer representing the parent node of the current node being processed, defaulting to None. The length of the neighbors list for the start node is not 1 or the first neighbor of the start node is not equal to the parent.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.append(not func_1(nodes, node, start))
        
    #State: Output State: `distances` is a list containing boolean values, each indicating whether the path from the start node to the respective child node (excluding the parent node) satisfies the condition defined in `func_1(nodes, node, start)`.
    return any(distances)
    #The program returns True if any of the paths from the start node to the respective child nodes satisfies the condition defined in `func_1(nodes, node, start)`, otherwise it returns False.
#Overall this is what the function does:The function accepts a dictionary `nodes` representing a tree structure, an integer `start` representing the starting node index, and an optional integer `parent` representing the parent node of the current node being processed (defaulting to None). It checks if any path from the start node to its child nodes satisfies a certain condition. If such a path exists, it returns `True`; otherwise, it returns `False`.

#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, edges is a list of tuples representing the edges of the tree, where each tuple (u, v) indicates an edge between nodes u and v, and start is an integer such that 1 ≤ start ≤ n, representing the starting node for the first round.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is still an empty list, `start` is an integer such that 1 ≤ start ≤ n, `empty` is still True, `nodes` is a defaultdict where each value is a list containing up to `n-1` integers representing the adjacent nodes to the corresponding key.
    #
    #Explanation: The loop iterates `n-1` times, each time reading two integers `u` and `v` from the input. It then adds `v` to the list of nodes connected to `u` and vice versa, updating the `nodes` defaultdict. Since the `edges` list is not modified within the loop, it remains empty. All other variables (`t`, `empty`, `start`) are not affected by the loop and thus remain in their initial states.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: Output State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is still an empty list, `start` is an integer such that 1 ≤ start ≤ n, `empty` is still True, `nodes` is a defaultdict where each value is a list containing up to `n-1` integers representing the adjacent nodes to the corresponding key, `leaves` is a deque containing all the keys from `nodes` whose length is 1.
    #
    #In this output state, the `leaves` deque contains all the nodes that are leaves (i.e., nodes with only one adjacent node) in the graph represented by the `nodes` defaultdict. The other variables remain unchanged from their initial states.
    start = int(input())
    moves = func_1(nodes, start)
    if moves :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: `moves` is the result of `func_1(nodes, start)`, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is still an empty list, `start` is an input integer, `empty` is still True, `nodes` is a defaultdict where each value is a list containing up to `n-1` integers representing the adjacent nodes to the corresponding key, `leaves` is a deque containing all the keys from `nodes` whose length is 1, and if `moves` is not empty, then the postcondition follows the conditions specified in the if part; otherwise, `moves` is an empty list.
#Overall this is what the function does:The function processes a tree structure defined by its number of nodes (n), a single tree level (t), a list of edges, and a starting node (start). It identifies all leaf nodes in the tree and then calls another function `func_1` with the tree structure and starting node. Based on the result of `func_1`, it prints either 'Ron' or 'Hermione'. The function ultimately determines which character ('Ron' or 'Hermione') wins based on the tree's structure and the starting node.

