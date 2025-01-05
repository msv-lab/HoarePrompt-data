#State of the program right berfore the function call: **Precondition**: **n, m, and D are integers such that 2 <= n <= 2 * 10^5, n - 1 <= m <= min(2 * 10^5, (n(n-1))/2), and 1 <= D < n. The input edges are represented as pairs of integers v_i, u_i (1 <= v_i, u_i <= n, u_i ≠ v_i) where each pair represents an edge between vertices v_i and u_i.**
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
        
    #State of the program after the  for loop has been executed: `n`, `m`, and `D` are assigned integer values, `ds` is a defaultdict with sets containing pairs of integers. Each pair `(s, f)` is added to `ds` and both `(s, f)` and `(f, s)` are added to `dmain` for all iterations of the loop.
    if (len(dmain[1]) < D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`n`, `m`, and `D` are assigned integer values. `ds` is a defaultdict with sets containing pairs of integers. Each pair `(s, f)` is added to `ds` and both `(s, f)` and `(f, s)` are added to `dmain` for all iterations of the loop. If the length of `dmain[1]` is less than `D`, then the program prints 'NO'.
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
        
    #State of the program after the loop has been executed: `n` is equal to the final value of `i`, all elements in `arr` have been updated based on the conditions in the loop, `cur` contains the final value of the counter used in the loop, `tov` is empty indicating the loop has finished executing
    if (cur > D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`n` is equal to the final value of `i`, all elements in `arr` have been updated based on the conditions in the loop, `cur` contains the final value of the counter used in the loop, `tov` is empty indicating the loop has finished executing. If `cur` is greater than `D`, the program prints 'NO'. Otherwise, there is no change in the program state.
    sviaz = set()
    ite = dmain[1].copy()
    for el in ite:
        if arr[el] not in sviaz:
            sviaz.add(arr[el])
        else:
            dmain[el].remove(1)
            dmain[1].remove(el)
        
    #State of the program after the  for loop has been executed: `n` is greater than 0, `tov` contains at least one element, `cur` is 0, `D` is adjusted accordingly, `sviaz` is initialized with at least one element, all elements in `ite` have been iterated over, and all conditions in the loop have been processed.
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
        
    #State of the program after the loop has been executed: Output State: sv is empty, vis contains all visited elements, res contains concatenated strings of all processed elements in the order they were appended, dmain is fully updated with corresponding elements removed. The loop will not execute again.
    print('\n'.join(res))
#Overall this is what the function does:The function `func` reads input values `n`, `m`, and `D` and processes pairs of integers representing edges between vertices. It populates dictionaries `ds` and `dmain` with the edge connections. It then performs various checks and manipulations on the input data to determine relationships between vertices and prints a specific output based on certain conditions. The function does not accept any parameters explicitly, but it processes input data according to specified constraints and prints the final result.

