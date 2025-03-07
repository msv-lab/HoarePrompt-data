#State of the program right berfore the function call: t is a positive integer, each test case consists of n and q where 2 ≤ n ≤ 2·10^5 and 1 ≤ q ≤ 2·10^5, a is a list of n integers where 0 ≤ a_i < 2^30, and each query is a pair of integers l and r where 1 ≤ l < r ≤ n.
def func_1():
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        q = int(data[index + 1])
        
        index += 2
        
        a = [0] * (n + 1)
        
        pf = [0] * (n + 1)
        
        mp = defaultdict(list)
        
        mp[0].append(0)
        
        for i in range(1, n + 1):
            a[i] = int(data[index])
            index += 1
            pf[i] = pf[i - 1] ^ a[i]
            mp[pf[i]].append(i)
        
        for _ in range(q):
            l = int(data[index])
            r = int(data[index + 1])
            index += 2
            x = pf[r] ^ pf[l - 1]
            if x == 0:
                results.append('YES')
                continue
            v1 = mp[pf[r]]
            v2 = mp[pf[l - 1]]
            it1 = bisect_left(v1, l)
            it2 = bisect_left(v2, r) - 1
            if it1 < len(v1) and it2 >= 0 and v1[it1] < v2[it2]:
                results.append('YES')
            else:
                results.append('NO')
        
    #State: `index` is 49, `q` is the original `q` minus 3, `results` is a list of 'YES' and 'NO' based on all the queries processed, and `a`, `pf`, and `mp` are reset to their initial states as defined in the initial state.
    print('\n'.join(results))
    #This is printed: YES\nNO\n... (where the list consists of 'YES' and 'NO' based on all the queries processed)
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t`, followed by `t` sets of data. Each set includes integers `n` and `q`, a list `a` of `n` integers, and `q` queries. For each query defined by integers `l` and `r`, it determines whether the XOR of the subarray from index `l` to `r-1` equals zero. If so, it appends 'YES' to the results; otherwise, it appends 'NO'. After processing all queries for each test case, it prints the results as a list of 'YES' and 'NO' strings.

