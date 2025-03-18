#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1) where 1 ≤ u_1 ≤ n, representing the starting node for the single round.
def func_1():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `n` is an integer read from input such that 2 ≤ n ≤ 2 × 10^5, `t` is 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1) where 1 ≤ u_1 ≤ n, representing the starting node for the single round. `edges` is an empty list. `empty` is True. `nodes` is a defaultdict of lists where each key is a node and the value is a list of adjacent nodes forming the tree.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: n is an integer read from input such that 2 ≤ n ≤ 2 × 10^5, t is 1, the tree is represented by n-1 edges where each edge is a pair of integers (u, v) with 1 ≤ u, v ≤ n, and the tree has exactly two leaves. The last line contains t integers (u_1) where 1 ≤ u_1 ≤ n, representing the starting node for the single round. edges is an empty list. empty is True. nodes is a defaultdict of lists where each key is a node and the value is a list of adjacent nodes forming the tree. ends is a list containing the two leaf nodes of the tree.
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
        
    #State: `tree` is a list containing the path from `s` to `e`, `prev` is `e`, `curr` is `e`.
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
    #State: `tree` is a list containing the path from `s` to `e` followed by `e`, `prev` is `e`, `curr` is `e`, `start` is an input integer, `idx` is the index of `start` in `tree`, and `moves` is a list `[idx, n - idx - 1]`. At least one of the elements in `moves` is odd, or all elements in `moves` are even numbers.
#Overall this is what the function does:The function determines the winner of a game played on a tree with exactly two leaves. Given the number of nodes `n`, a list of edges representing the tree, and a starting node `u_1`, it calculates the path between the two leaves and checks the distance from the starting node to each leaf. If either distance is odd, Ron wins; otherwise, Hermione wins. The function prints the name of the winner.

