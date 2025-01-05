#State of the program right berfore the function call: 
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
        
    #State of the program after the  for loop has been executed: `n`, `m`, and `D` are integers obtained by splitting the input line on spaces; `ds` is a defaultdict with a set containing all pairs of `f` and `s` from the input; `dmain` is a defaultdict with sets containing all pairs of `f` and `s` from the input
    if (len(dmain[1]) < D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *`n`, `m`, and `D` are integers obtained by splitting the input line on spaces; `ds` is a defaultdict with a set containing all pairs of `f` and `s` from the input; `dmain` is a defaultdict with sets containing all pairs of `f` and `s` from the input. If the length of the set in `dmain` corresponding to key 1 is less than `D`, 'NO' is printed. Otherwise, no changes are made to the variables.
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
        
    #State of the program after the loop has been executed: `n`, `m`, `D`, `ds`, `dmain`, `arr`, `i`, and `cur` have their final values after the loop finishes executing. All elements in `ds` will have their corresponding `arr` values updated to `cur`. The loop control variable `i` will have a final value after the loop finishes.
    if (cur > D) :
        print('NO')
        exit()
    #State of the program after the if block has been executed: *All elements in `ds` have their corresponding `arr` values updated to `cur`, `i` has its final value after the loop finishes, `cur` is greater than `D`, and 'NO' is printed.
    sviaz = set()
    ite = dmain[1].copy()
    for el in ite:
        if arr[el] not in sviaz:
            sviaz.add(arr[el])
        else:
            dmain[el].remove(1)
            dmain[1].remove(el)
        
    #State of the program after the  for loop has been executed: `sviaz` contains the unique elements from index 1 of set `dmain` and array `arr`, `ite` is not empty, `el` is the last element in `ite` such that `arr[el]` is not in `sviaz` for the loop to execute, `dmain` may have removed elements based on the loop's condition
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
        
    #State of the program after the loop has been executed: `sviaz` contains the unique elements from index 1 of set `dmain` and array `arr`, `ite` is not empty, `el` is the last element in `ite` such that `arr[el]` is not in `sviaz`, `dmain` may have removed elements based on the loop's condition, `sv` is empty, `vis` contains all unique elements visited in the loop, `res` is a list containing all concatenated strings of `nxt` and `el`, `nxt` is the last popped element from `sv`
    print('\n'.join(res))
#Overall this is what the function does:The function does not accept any parameters. It reads input values, processes the data to form relationships between elements, and then performs a series of operations based on those relationships. It checks specific conditions and prints outputs accordingly. The function outputs a series of concatenated strings if certain conditions are met.

