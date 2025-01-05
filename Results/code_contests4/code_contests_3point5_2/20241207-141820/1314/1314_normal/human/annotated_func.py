#State of the program right berfore the function call: **Precondition**: **n, m, D are integers such that 2 ≤ n ≤ 2 ⋅ 10^5, n - 1 ≤ m ≤ min(2 ⋅ 10^5, (n(n-1))/(2)), 1 ≤ D < n. The input edges are represented as pairs of integers v_i, u_i (1 ≤ v_i, u_i ≤ n, u_i ≠ v_i).**
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
        
    #State of the program after the  for loop has been executed: `n`, `m`, `D` are integers satisfying the given constraints, `ds` is a defaultdict containing sets where `ds[s]` contains all the values of `f` added throughout the loop, `dmain` is a defaultdict containing sets where `dmain[s]` contains the values of `f` added throughout the loop
    if (len(dmain[1]) < D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`n`, `m`, `D` are integers satisfying the given constraints. `ds` is a defaultdict containing sets where `ds[s]` contains all the values of `f` added throughout the loop. `dmain` is a defaultdict containing sets where `dmain[s]` contains the values of `f` added throughout the loop. If the length of `dmain[1]` is less than `D`, 'NO' is printed.
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
        
    #State of the program after the loop has been executed: `n`, `m`, `D` are integers satisfying the given constraints. `ds` and `dmain` are default dictionaries. `arr` is a list of size `n + 1` where each element represents the group number it belongs to. `i` is equal to `n`, `cur` is the total number of groups, `tov` is empty, `nxt` is None. All elements in `ds` have been processed and grouped accordingly, and all elements in `arr` have been updated with their corresponding group numbers.
    if (cur > D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *All variables remain unchanged. If `cur` is greater than `D`, the program prints 'NO' to the console.
    sviaz = set()
    ite = dmain[1].copy()
    for el in ite:
        if arr[el] not in sviaz:
            sviaz.add(arr[el])
        else:
            dmain[el].remove(1)
            dmain[1].remove(el)
        
    #State of the program after the  for loop has been executed: `sviaz` contains elements from `arr` at certain indices, `ite` is empty, `el` is the last element iterated in the loop, `dmain[1]` may have elements removed depending on the condition met in the loop.
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
        
    #State of the program after the loop has been executed: `sviaz` contains elements from `arr` at certain indices, `ite` is empty, `el` is the last element iterated in the loop, `dmain[1]` may have elements removed, `sv` is empty, `vis` contains all unique elements visited during the loop, `res` is a list containing the string 'YES' with the appended values of `nxt` and `el` for each iteration, all elements in `dmain` have been modified based on the loop conditions, `nxt` is empty, `el` is the last element iterated in the loop, and `dmain[nxt]` is empty
    print('\n'.join(res))
#Overall this is what the function does:The function `func` reads input values and processes them to determine certain relationships between elements. It checks conditions based on these relationships and prints the results accordingly. However, the code does not return any value.

