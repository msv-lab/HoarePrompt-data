#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2×10^5, t is an integer such that t = 1, the next n-1 lines each contain two integers 1 ≤ u, v ≤ n representing the edges of the tree, and the last line contains t integers 1 ≤ u_1, ..., u_t ≤ n representing the starting nodes for each round. It is guaranteed that the tree has exactly two leaves.
def func_1():
    n, t = map(int, input().split())
    edges = []
    empty = True
    nodes = defaultdict(list)
    for i in range(n - 1):
        u, v = map(int, input().split())
        
        nodes[u].append(v)
        
        nodes[v].append(u)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is an empty list, `empty` is `True`, `nodes` is a defaultdict of lists representing the adjacency list of the tree, `i` is n-2.
    ends = []
    for key in nodes:
        if len(nodes[key]) == 1:
            ends.append(key)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is an empty list, `empty` is `True`, `nodes` is a defaultdict of lists representing the adjacency list of the tree, `i` is n-2, and `ends` is a list containing all the keys from the `nodes` dictionary that have a length of 1.
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
        
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is an empty list, `empty` is `True`, `nodes` is a defaultdict of lists representing the adjacency list of the tree, `i` is n-2, `ends` is a list containing all the keys from the `nodes` dictionary that have a length of 1, `s` is the first element of `ends`, `e` is the second element of `ends`, `tree` is a list containing all nodes from `s` to `e`, inclusive, `prev` is `e`, `curr` is `e`.
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
    #State: `n` is an integer such that 2 ≤ n ≤ 2×10^5, `t` is 1, `edges` is an empty list, `empty` is `True`, `nodes` is a defaultdict of lists representing the adjacency list of the tree, `i` is n-2, `ends` is a list containing all the keys from the `nodes` dictionary that have a length of 1, `s` is the first element of `ends`, `e` is the second element of `ends`, `tree` is a list containing all nodes from `s` to `e`, inclusive, with `e` appended again, `prev` is `e`, `curr` is `e`, `start` is an input integer, `idx` is the index of `start` in `tree`, `moves` is `[idx, n - idx - 1]`. At least one element in `moves` is odd if the if condition is met, otherwise, all elements in `moves` are even numbers.
#Overall this is what the function does:The function `func_1` determines the winner of a game played on a tree structure. Given the number of nodes `n` in a tree with exactly two leaves and the edges of the tree, along with a starting node, it prints 'Ron' if the number of moves to reach either leaf from the starting node is odd, otherwise it prints 'Hermione'.

