#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer such that 1 ≤ u_1 ≤ n.
def func_1():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `t` is 1, `u` is an input integer, `v` is an input integer, `n` is an integer such that 2 ≤ n ≤ 2×10^5, `empty` is True, `nodes` is a defaultdict with default factory list, `i` is n-1, every node in `nodes` has its corresponding neighbors appended.
    #
    #Explanation: After the loop executes all its iterations (i.e., `i` goes from 0 to `n-2`), the variable `i` will be equal to `n-1`. During each iteration, the loop reads two integers `u` and `v`, and appends `v` to the list of neighbors of `u` and vice versa. This process continues until all possible edges are added to the graph represented by the `nodes` defaultdict. The `empty` variable remains True as it was not modified within the loop, and `t`, `u`, and `v` retain their last assigned values from the input.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: All keys from the `nodes` dictionary that have a list of length exactly 1 have been appended to the `ends` list.
    s, e = list(ends)
    tree = [s]
    prev = s
    curr = nodes[s][0]
    while curr != e:
        tree.append(curr)
        
        if nodes[curr][0] == prev:
            prev = curr
            curr = nodes[curr][1]
        else:
            prev = curr
            curr = nodes[curr][0]
        
    #State: Output State: The `tree` list will contain a path from `s` to `e` in the graph represented by `nodes`. Specifically, starting from `s`, the `tree` list will include each node visited until it reaches `e`. The `prev` variable will hold the last node that was visited before `e`, and `curr` will be equal to `e` after the loop finishes. The `tree` list will trace the path from `s` to `e` based on the structure defined by `nodes`.
    #
    #In simpler terms, the `tree` list will show the sequence of nodes traversed from the start node `s` to the end node `e` following the rules specified in the `nodes` dictionary, with `prev` holding the last node before `e` and `curr` being set to `e` at the end.
    tree.append(e)
    start = int(input())
    idx = tree.index(start)
    moves = [idx, n - idx - 1]
    if any([(move % 2 == 1) for move in moves]) :
        print('Ron')
        #This is printed: Ron
    else :
        print('Hermione')
        #This is printed: Hermione
    #State: Postcondition: `tree` list includes the node `e`; `prev` holds the last node that was visited before `e`; `curr` is equal to `e`; `start` is an input integer; `idx` is the index of `start` in the `tree` list; `moves` is `[idx, n - idx - 1]`. If at least one move in `moves` is an odd number, the condition remains as is. If all elements in `moves` are even numbers, the condition also remains as is.
#Overall this is what the function does:The function processes a graph represented by a defaultdict of nodes and their neighbors. It identifies leaf nodes (nodes with only one neighbor) and constructs a path from one specified node (`s`) to another (`e`). Based on the indices of the start node within this path, it determines whether "Ron" or "Hermione" is printed. If the sum of the indices of the start node and the remaining nodes in the path is odd, "Ron" is printed; otherwise, "Hermione" is printed.

