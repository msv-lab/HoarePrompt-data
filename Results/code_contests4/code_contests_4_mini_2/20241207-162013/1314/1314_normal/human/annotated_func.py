#State of the program right berfore the function call: n is an integer representing the number of vertices in the graph (2 ≤ n ≤ 200000), m is an integer representing the number of edges in the graph (n - 1 ≤ m ≤ min(200000, (n(n-1))/(2))), D is an integer representing the required degree of the first vertex (1 ≤ D < n), and the edges are defined by m pairs of integers (v_i, u_i) where 1 ≤ v_i, u_i ≤ n and v_i ≠ u_i, ensuring no self-loops or multiple edges exist.
def func():
    sys.stdin = BytesIO(sys.stdin.read())
    input = lambda : sys.stdin.readline().rstrip('\r\n')
    n, m, D = [int(x) for x in input().split(' ')]
    ds = defaultdict(set)
    dmain = defaultdict(set)
    for i in range(m):
        s, f = [int(x) for x in input().split(' ')]
        
        if s != 1 and f != 1:
            ds[s].add(f)
            ds[f].add(s)
        
        dmain[s].add(f)
        
        dmain[f].add(s)
        
    #State of the program after the  for loop has been executed: `n` is an integer, `m` is a non-negative integer, `D` is an integer, `ds` is a defaultdict with sets containing pairs of integers except when both are 1, `dmain` is a defaultdict with sets containing all pairs of integers, and `i` is equal to `m - 1` after the last iteration.
    if (len(dmain[1]) < D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`n` is an integer, `m` is a non-negative integer, `D` is an integer, `ds` is a defaultdict with sets containing pairs of integers except when both are 1, `dmain` is a defaultdict with sets containing all pairs of integers, `i` is equal to `m - 1` after the last iteration. If the length of `dmain[1]` is less than `D`, then 'NO' is printed.
    arr = [0] * (n + 1)
    i = 2
    cur = 0
    while i < n:
        if arr[i] == 0:
            cur += 1
            tov = {i}
            arr[i] = cur
            while len(tov):
                nxt = tov.pop()
                for el in ds[nxt]:
                    if arr[el] == 0:
                        arr[el] = cur
                        tov.add(el)
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to `n`, `arr` contains values assigned to `cur` at all indices that were previously 0, `cur` is the next value after the last assigned value, `tov` is empty, `nxt` is not applicable, `ds` has been completely processed for all elements that were in `tov`, and all elements in `arr` corresponding to reachable indices from the original 0 entries have been assigned the same value of `cur`.
    if (cur > D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`i` is equal to `n`, `arr` contains values assigned to `cur` at all indices that were previously 0, `cur` is greater than `D`, `tov` is empty, `nxt` is not applicable, `ds` has been completely processed for all elements that were in `tov`, and all elements in `arr` corresponding to reachable indices from the original 0 entries have been assigned the same value of `cur`. The program execution has been terminated.
    sviaz = set()
    ite = dmain[1].copy()
    for el in ite:
        if arr[el] not in sviaz:
            sviaz.add(arr[el])
        else:
            dmain[el].remove(1)
            dmain[1].remove(el)
        
    #State of the program after the  for loop has been executed: `i` is equal to `n`, `arr` contains values assigned to `cur` at all indices that were previously 0, `cur` is greater than `D`, `tov` is empty, `nxt` is not applicable, `ds` has been completely processed for all elements that were in `tov`, all elements in `arr` corresponding to reachable indices from the original 0 entries have been assigned the same value of `cur`, `sviaz` contains all unique values from `arr` that were encountered during the loop, and `dmain[1]` contains only those elements which were not equal to `arr[el]` for any `el` that was in `ite`.
    sv = set()
    sv.add(1)
    vis = set()
    vis.add(1)
    res = ['YES']
    while len(sv):
        nxt = sv.pop()
        
        for el in dmain[nxt]:
            if el not in vis:
                sv.add(el)
                vis.add(el)
                res.append(str(nxt) + ' ' + str(el))
            dmain[el].remove(nxt)
        
    #State of the program after the loop has been executed: `i` is equal to `n`, `nxt` is no longer applicable, `dmain` contains only elements that were not connected to any processed `nxt`, `sv` is empty, `vis` contains all unique values that were seen during the loop, and `res` contains all pairs of processed `nxt` and unique `el` values that were added during the loop.
    print('\n'.join(res))
#Overall this is what the function does:The function accepts integers `n`, `m`, and `D`, along with a list of edges represented by pairs of integers. It checks if vertex 1 has at least `D` connections; if not, it outputs 'NO'. It then verifies if the number of connected components (excluding vertex 1) exceeds `D`, again outputting 'NO' if this is the case. Finally, the function constructs and prints the connections in a specific format if the conditions are met. The function does not return a value but prints results directly to standard output.

