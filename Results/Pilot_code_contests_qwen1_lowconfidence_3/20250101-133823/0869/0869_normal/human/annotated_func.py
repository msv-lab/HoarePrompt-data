#State of the program right berfore the function call: The input is a list of tuples, where each tuple contains two integers representing the indexes of cities connected by a stamp. The length of this list is n (1 ≤ n ≤ 10^5), and each city index is an integer from 1 to 10^9. All city indexes are unique within each tuple, and the sequence of stamps corresponds to a valid route from one city to another without visiting any city more than once.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer input from the user, `nbr` is a dictionary where each key is a string and its value is a list of strings, `cand` is a set containing strings. For every pair of strings `(a, b)` where `a` is a key in `nbr` and `b` is in `nbr[a]`, there is an entry in `nbr[b]` that is `a`, and `cand` contains `b` if and only if `b` was added to `nbr` as a new key.
    for v in cand:
        break
        
    #State of the program after the  for loop has been executed: `n` is an integer input from the user, `nbr` is a dictionary where each key is a string and its value is a list of strings, `cand` is a set containing strings that must be non-empty. The loop will always execute exactly once, as long as `cand` is non-empty, and the loop body does nothing (it just breaks out of the loop immediately). After the loop, `v` is any element of `cand`.
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
        
    #State of the program after the loop has been executed: `Q` is empty, `marked` contains all nodes reachable from the initial node `v` without cycles, `res` contains all unique nodes reachable from `v` without cycles, `v` is the last node processed in `Q`.
    print(' '.join(res))
#Overall this is what the function does:The function processes a list of tuples representing connections between cities. It constructs a graph where each city is a node and each tuple represents an edge connecting two cities. The function then performs a breadth-first search (BFS) starting from a randomly chosen node (determined by the `cand` set). The BFS ensures that no city is visited more than once and constructs a list (`res`) containing all unique cities reachable from the starting node. Finally, it prints the list of reachable cities in the order they were discovered. The function handles edge cases such as an empty input list or a single node graph. However, it does not handle disconnected graphs; in such cases, it only processes one connected component.

