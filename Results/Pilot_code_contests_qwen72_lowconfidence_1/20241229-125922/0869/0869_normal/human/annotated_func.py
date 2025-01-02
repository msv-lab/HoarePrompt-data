#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 105), and the subsequent n lines contain pairs of distinct positive integers representing the stamps, where each integer is between 1 and 109.
def func():
    n = int(raw_input())
    nbr = dict()
    cand = set()
    for i in range(n):
        l = raw_input().split()
        
        if l[0] not in nbr:
            nbr[l[0]] = [l[1]]
            cand.add(l[0])
        else:
            nbr[l[0]].append(l[1])
            cand.remove(l[0])
        
        if l[1] not in nbr:
            nbr[l[1]] = [l[0]]
            cand.add(l[1])
        else:
            nbr[l[1]].append(l[0])
            cand.remove(l[1])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 105), `i` is `n - 1`, `nbr` is a dictionary where each key is a string representing a stamp and each value is a list of strings representing the stamps that are connected to the key stamp. `cand` is a set containing the stamps that are not connected to any other stamp in the final state. If `n` is 0, the loop does not execute, and `nbr` remains an empty dictionary, and `cand` remains an empty set.
    for v in cand:
        break
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 105), `i` is `n - 1`, `nbr` is a dictionary where each key is a string representing a stamp and each value is a list of strings representing the stamps that are connected to the key stamp, `cand` is a set containing the stamps that are not connected to any other stamp in the final state. If `cand` is non-empty, the loop executes once and then breaks. If `cand` is empty, the loop does not execute.
    marked = set()
    marked.add(v)
    res = [v]
    Q = [v]
    while len(Q) > 0:
        v = Q.pop()
        
        for i in nbr[v]:
            if i not in marked:
                marked.add(i)
                res.append(i)
                Q.append(i)
        
    #State of the program after the loop has been executed: `n` is a positive integer (1 ≤ n ≤ 105), `i` is no longer relevant, `nbr` is a dictionary where each key is a string representing a stamp and each value is a list of strings representing the stamps that are connected to the key stamp, `cand` is a set containing the stamps that are not connected to any other stamp in the final state, `marked` contains all stamps that are reachable from the initial value of `v` through the connections defined in `nbr`, `res` contains the sequence of stamps visited starting from the initial value of `v`, and `Q` is empty.
    print(' '.join(res))
#Overall this is what the function does:The function `func` reads a series of `n` pairs of distinct positive integers (stamps) from the standard input. Each pair represents a connection between two stamps. The function constructs a graph where each stamp is a node and each pair represents an undirected edge between two nodes. It identifies the set of stamps that are not connected to any other stamp (`cand`). If there are any such stamps, it selects one and performs a depth-first search (DFS) starting from that stamp to find all connected stamps. The function then prints the sequence of stamps visited during the DFS in the order they were visited. If no unconnected stamps exist, the function will still perform a DFS starting from an arbitrary stamp, but the behavior is not clearly defined in the code (it will start from the first stamp in the `cand` set, which may be empty). The final state of the program includes a dictionary `nbr` representing the graph, a set `cand` of unconnected stamps, a set `marked` of visited stamps, and a list `res` of the sequence of stamps visited during the DFS. If `n` is 0, the function will print an empty list.

