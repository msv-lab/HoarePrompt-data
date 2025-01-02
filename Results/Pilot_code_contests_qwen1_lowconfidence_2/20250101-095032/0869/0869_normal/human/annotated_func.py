#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 10^5, and each stamp is represented by two integers indicating the indexes of the cities between which the letter is sent, where the indexes are integers from 1 to 10^9, and all indexes are unique within a single test case.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range of 1 to \(10^5\), `nbr` is a dictionary where each key is a node and its value is a list of connected nodes, `cand` is a set containing all unique nodes that were added to the dictionary, and `l` is the list of strings derived from user input.
    for v in cand:
        break
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range of 1 to \(10^5\), `nbr` is a dictionary where each key is a node and its value is a list of connected nodes, `cand` is a set containing all unique nodes that were added to the dictionary (must contain at least one element), `v` is the last node in the set `cand`, and we break out of the most internal loop or if statement we were directly inside.
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
        
    #State of the program after the loop has been executed: `v` is the last element of the original `cand`, `Q` is empty, `marked` contains all nodes directly or indirectly reachable from the original `v` including all nodes in `nbr[v]` and any other nodes reachable through them, `res` contains all nodes directly or indirectly reachable from the original `v` including all nodes in `nbr[v]` and any other nodes reachable through them.
    print(' '.join(res))
#Overall this is what the function does:The function processes an integer \( n \) representing the number of stamps, along with the indexes of the cities for each stamp. It constructs a graph where each city is a node and each stamp represents an edge connecting two nodes. The function then performs a breadth-first search (BFS) starting from any node in the graph to find and print all nodes that are directly or indirectly reachable from that starting node. If the input is valid, the function prints a list of all reachable nodes; otherwise, it does not return anything meaningful due to the lack of explicit error handling.

