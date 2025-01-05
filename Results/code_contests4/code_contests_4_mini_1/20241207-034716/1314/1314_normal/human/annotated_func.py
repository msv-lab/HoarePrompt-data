#State of the program right berfore the function call: n is an integer (2 ≤ n ≤ 2 ⋅ 10^5), m is an integer (n - 1 ≤ m ≤ min(2 ⋅ 10^5, (n(n-1))/(2))), D is an integer (1 ≤ D < n), and the edges are given as pairs of integers (v_i, u_i) where 1 ≤ v_i, u_i ≤ n and v_i ≠ u_i, ensuring there are no self-loops or multiple edges.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer (2 ≤ n ≤ 2 ⋅ 10^5), `m` is an integer (n - 1 ≤ m ≤ min(2 ⋅ 10^5, (n(n-1))/(2))), `D` is an integer (1 ≤ D < n), `ds` is a defaultdict of sets containing pairs of integers from input excluding 1, `dmain` is a defaultdict of sets containing all pairs of integers from input, and `i` is equal to `m - 1`.
    if (len(dmain[1]) < D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`n`, `m`, `D`, `ds`, `dmain`, and `i` are integers and collections. If the length of `dmain[1]` is less than `D`, 'NO' is printed and the program exits. If the length of `dmain[1]` is greater than or equal to `D`, the execution continues beyond this point without any specific action taken on this condition.
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
        
    #State of the program after the loop has been executed: `i` is `n`, `cur` is equal to the total number of unique elements in `ds` that were originally 0 in `arr`, `arr` contains values assigned to all elements that were originally 0 and correspond to the elements in `ds` that are reachable from the initial `tov`, `tov` is empty, `n` is greater than 2, and `m`, `D`, `ds`, and `dmain` remain unchanged.
    if (cur > D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`i` is `n`, `cur` is equal to the total number of unique elements in `ds` that were originally 0 in `arr`, `arr` contains values assigned to all elements that were originally 0 and correspond to the elements in `ds` that are reachable from the initial `tov`, `tov` is empty, `n` is greater than 2, `m`, `D`, `ds`, and `dmain` remain unchanged. If `cur` is greater than `D`, the program exits.
    sviaz = set()
    ite = dmain[1].copy()
    for el in ite:
        if arr[el] not in sviaz:
            sviaz.add(arr[el])
        else:
            dmain[el].remove(1)
            dmain[1].remove(el)
        
    #State of the program after the  for loop has been executed: `i` is `n`, `cur` is equal to the total number of unique elements in `ds` that were originally 0 in `arr`, `tov` is empty, `n` is greater than 2, `m`, `D`, `ds`, and `dmain` remain unchanged; `sviaz` contains all unique values from `arr` that were encountered, `dmain[el]` may have had elements removed based on the intersection with `sviaz`.
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
        
    #State of the program after the loop has been executed: `i` is `n + k + m` (where `k` is the total number of unique elements processed from `dmain`), `cur` is equal to the total number of unique elements in `ds` that were originally 0 in `arr`, `tov` is empty, `n` is greater than 2, `m`, `D`, `ds`, and `dmain` remain unchanged, `sv` contains all unique values from `dmain` that were encountered, `vis` contains 1 and all unique `el` values added during the loop, `res` contains `['YES']` followed by strings for each unique `el` processed, and `sv` is empty as it has been fully processed.
    print('\n'.join(res))
#Overall this is what the function does:The function processes a graph represented by edges, where it checks if the number of connections from vertex 1 is at least D. If not, it outputs 'NO' and exits. It performs a traversal to group connected nodes and checks if the number of unique groups exceeds D, outputting 'NO' if it does. Finally, it constructs and prints the connections starting from vertex 1, outputting 'YES' followed by the connections formed. The function does not accept parameters and operates on input read from standard input.

