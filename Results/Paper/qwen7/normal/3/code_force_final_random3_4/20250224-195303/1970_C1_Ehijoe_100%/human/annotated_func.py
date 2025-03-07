#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer 1 ≤ u_1 ≤ n.
def func_1():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: Output State: `i` is `n-2`; `n` must be at least 2; `u` is an input integer; `v` is an input integer; `nodes[v]` contains all integers from 1 to n that are connected to `v` through the edges provided by the input.
    #
    #Explanation: After the loop has executed all its iterations (i.e., `i` goes from 0 to `n-2`), the final value of `i` will be `n-2`. The variable `u` and `v` will contain the integers read from the input during each iteration. The `nodes` dictionary will have been updated such that for each node `v` (where `1 ≤ v ≤ n`), the list `nodes[v]` will include all nodes `u` that are connected to `v` via the edges specified in the input.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: Output State: The variable `ends` will contain a list of all keys from the dictionary `nodes` whose corresponding value lists (i.e., `nodes[key]`) have a length of exactly one. The variable `nodes[key]` remains unchanged after the loop completes. The variable `i` starts at `n-2` and decreases by 1 in each iteration until it reaches -1 (assuming `i` is decremented within the loop or elsewhere in the code), but its final state is not relevant to the output state of `ends`.
    #
    #In simpler terms, after the loop has executed all its iterations, `ends` will include every key from `nodes` that points to a list containing exactly one element.
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
        
    #State: Output State: The variable `prev` is equal to `curr`, `tree` contains all elements from `s` up to and including `e`, and `curr` is equal to `e`.
    #
    #Explanation: After the loop completes all its iterations, `curr` will eventually become equal to `e` because the loop continues to iterate as long as `curr` is not equal to `e`. Since `prev` is always set to `curr` at the end of each iteration, `prev` will also be equal to `curr` when the loop ends. The `tree` list will contain all the elements traversed from `s` to `e`, forming a path in the graph defined by the `nodes` dictionary.
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
    #State: Postcondition: `prev` is equal to `curr`, `tree` contains all elements from `s` up to and including `e`, `curr` is equal to `e`, `idx` is the index of `start` in `tree`, `moves` is `[idx, n - idx - 1]`. If at least one move in `moves` is an odd number, the condition remains as is. If none of the moves in `moves` are odd numbers, the condition also remains as is.
#Overall this is what the function does:The function reads the number of nodes \( n \) and edges \( t \) from input, constructs a graph using the given edges, identifies leaf nodes, and then finds a path between two specified nodes \( s \) and \( e \). It calculates the indices of these nodes in the path and determines whether the sum of these indices is odd or even, printing "Ron" if the sum is odd and "Hermione" if the sum is even.

