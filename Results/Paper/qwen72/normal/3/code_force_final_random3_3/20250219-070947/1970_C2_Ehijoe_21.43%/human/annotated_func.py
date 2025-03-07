#State of the program right berfore the function call: nodes is a dictionary or list representing the adjacency list of a tree with n nodes, start is an integer representing the starting node (1 ≤ start ≤ n), and parent is an integer or None, representing the parent node of the starting node in the tree.
def func_1(nodes, start, parent):
    if (len(nodes[start]) == 1 and nodes[start][0] == parent) :
        return [0]
        #The program returns a list containing the single element 0.
    #State: nodes is a dictionary or list representing the adjacency list of a tree with n nodes, start is an integer representing the starting node (1 ≤ start ≤ n), and parent is an integer or None, representing the parent node of the starting node in the tree. The length of nodes[start] is not 1, or if it is 1, then nodes[start][0] is not equal to parent.
    distances = []
    for node in nodes[start]:
        if node != parent:
            distances.extend([(1 + dist) for dist in func_1(nodes, node, start)])
        
    #State: `nodes[start]` has been fully iterated. `distances` is a list that contains all the values, each of which is 1 plus the corresponding value returned by `func_1(nodes, node, start)` for each `node` in `nodes[start]` that is not equal to `parent`.
    return distances
    #The program returns a list `distances` where each value is 1 plus the corresponding value returned by `func_1(nodes, node, start)` for each `node` in `nodes[start]` that is not equal to `parent`.
#Overall this is what the function does:The function `func_1` accepts parameters `nodes`, `start`, and `parent`. It returns a list of distances from the starting node to all its child nodes in the tree, where each distance is incremented by 1 for each level of depth. If the starting node has no children (or all children are the parent node), the function returns a list containing the single element 0. Otherwise, it returns a list of distances to all child nodes that are not the parent node.

#State of the program right berfore the function call: n is an integer such that 2 <= n <= 2 * 10^5, t is an integer and t = 1, nodes is a dictionary where each key is an integer representing a node and each value is a list of integers representing the neighbors of that node, start is an integer such that 1 <= start <= n.
def func_2():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `n` must be greater than 1, `i` is `n-2`, `nodes` is a defaultdict where each key is an integer representing a node and each value is a list of integers representing the neighbors of that node. Each node in the `nodes` dictionary will have a list of its neighbors, and the number of times each neighbor appears in the list will be equal to the number of times that neighbor was connected to the node during the loop's execution.
    leaves = deque()
    for key in nodes:
        if len(nodes[key]) == 1:
            leaves.append(key)
        
    #State: `n` is greater than 1, `i` is `n-2`, `nodes` is a defaultdict with all keys processed. `leaves` is a deque containing all keys from `nodes` that have exactly one neighbor.
    start = int(input())
    moves = func_1(nodes, start)
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: *`n` is greater than 1, `i` is `n-2`, `nodes` is a defaultdict with all keys processed, `leaves` is a deque containing all keys from `nodes` that have exactly one neighbor, `start` is an input integer, `moves` is the result of `func_1(nodes, start)`. If at least one element in `moves` is an odd number, the function behaves accordingly to the if part. If all elements in `moves` are even, the function behaves accordingly to the else part.
#Overall this is what the function does:The function `func_2` reads an integer `n` and an integer `t` from the input, where `2 <= n <= 2 * 10^5` and `t = 1`. It then reads `n - 1` pairs of integers representing edges between nodes and constructs a dictionary `nodes` where each key is a node and each value is a list of its neighbors. The function identifies all leaf nodes (nodes with exactly one neighbor) and stores them in a deque `leaves`. It reads another integer `start` from the input, where `1 <= start <= n`, and calls a function `func_1` with `nodes` and `start` as arguments, which returns a list of integers `moves`. If any integer in `moves` is odd, the function prints 'Ron'. Otherwise, it prints 'Hermione'. The function does not return any value.

