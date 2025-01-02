#State of the program right berfore the function call: n, m, v are integers such that 3 ≤ n ≤ 105, 0 ≤ m ≤ 105, 1 ≤ v ≤ n, where n represents the number of servers, m represents the number of direct connections, and v represents the index of the server whose failure will disconnect the system.
def func():
    n, m, v = map(int, raw_input().split())
    if (m < n - 1) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *`n`, `m`, and `v` are integers such that 3 ≤ n ≤ 105, 0 ≤ m ≤ 105, 1 ≤ v ≤ n. If `m` < `n - 1`, `-1` has been printed and the program has terminated.
    edges = [(i, i + 1) for i in xrange(n - 1)]
    m = m - len(edges)
    node1_nr = 1
    while m > 0 and node1_nr < n:
        node2_nr = node1_nr + 2
        
        while m > 0 and node2_nr < n:
            edges.append((node1_nr, node2_nr))
            m -= 1
            node2_nr += 1
        
        node1_nr += 1
        
    #State of the program after the loop has been executed: `n` is unchanged, `m` is the original value of `m` minus the total number of edges added, `v` is an integer such that 1 ≤ v ≤ n, `edges` is a list of tuples `[(i, i + 1) for i in range(n - 1)]` plus additional tuples `(node1_nr, node2_nr)` for each valid pair where `node1_nr` ranges from 1 to `n-1` and `node2_nr` ranges from `node1_nr + 2` to `n-1` while `m > 0`, `node1_nr` is `n`, `node2_nr` is `n` or greater.
    if (m > 0) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *`n` is unchanged, `m` is the original value of `m` minus the total number of edges added, `v` is an integer such that 1 ≤ v ≤ n, `edges` is a list of tuples `[(i, i + 1) for i in range(n - 1)]` plus additional tuples `(node1_nr, node2_nr)` for each valid pair where `node1_nr` ranges from 1 to `n-1` and `node2_nr` ranges from `node1_nr + 2` to `n-1` while `m > 0`, `node1_nr` is `n`, `node2_nr` is `n` or greater. If `m` > 0, the program has terminated.
    translate = [(i + 1) for i in xrange(n)]
    translate[v - 1], translate[1] = translate[1], translate[v - 1]
    output = [('%d %d' % (translate[n1], translate[n2])) for n1, n2 in edges]
    print('\n'.join(output))
#Overall this is what the function does:The function `func` reads three integers `n`, `m`, and `v` from the input, representing the number of servers, the number of direct connections, and the index of the server whose failure will disconnect the system, respectively. It then constructs a network of `n` servers with `m` connections in such a way that the network remains connected unless the server `v` fails. If it is impossible to construct such a network with the given `m` connections, the function prints `-1` and terminates. Otherwise, it prints the connections in the form of pairs of server indices. The function does not return any value; its primary action is to print the result to the console. The final state of the program is that the network configuration is printed, or `-1` is printed if the construction is not possible.

