#State of the program right berfore the function call: n is an integer representing the number of servers, m is an integer representing the number of direct connections, and v is an integer representing the index of the failing server such that 3 ≤ n ≤ 10^5, 0 ≤ m ≤ 10^5, and 1 ≤ v ≤ n.
def func():
    n, m, v = map(int, raw_input().split())
    if (m < n - 1) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *`n`, `m`, and `v` are integers. If `m` is less than `n - 1`, the postcondition remains as the preconditions where `m` is less than `n - 1`. There is no change to the values of `n` and `v` in this case. Since there is no else part, the postcondition does not change from the precondition unless the if condition is satisfied.
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
        
    #State of the program after the loop has been executed: `n` is an integer, `m` is 0, `v` is an integer, `edges` is the initial list of tuples `[ (0, 1), (1, 2), ..., ((n-2), (n-1)) ]`, `node1_nr` is 1, `node2_nr` is undefined
    if (m > 0) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *`n` is an integer, `m` is 0, `v` is an integer, `edges` is the initial list of tuples `[ (0, 1), (1, 2), ..., ((n-2), (n-1)) ]`, `node1_nr` is 1, `node2_nr` is undefined. If `m > 0`, then the value `-1` is printed. Otherwise, the state remains unchanged.
    translate = [(i + 1) for i in xrange(n)]
    translate[v - 1], translate[1] = translate[1], translate[v - 1]
    output = [('%d %d' % (translate[n1], translate[n2])) for n1, n2 in edges]
    print('\n'.join(output))
#Overall this is what the function does:The function `func()` takes three parameters: `n` (number of servers), `m` (number of direct connections), and `v` (index of the failing server). It constructs a network of servers connected by direct links under certain conditions and then reconfigures the network after the failure of one server. Specifically, the function first checks if the number of direct connections is sufficient for a fully connected network minus one server (i.e., \(m \geq n-1\)). If not, it prints `-1` and exits. Otherwise, it builds an initial set of direct connections between servers and further adds additional connections to ensure the remaining direct connections are used up. If any direct connections are still left over after the initial setup, it prints `-1` and exits. Finally, it reorders the server indices to reflect the failure of server `v` and prints out the new configuration of direct connections between the servers.

