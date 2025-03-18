#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5; a is a list of n integers where 0 ≤ a_i < 2^{30}; for each query, l and r are integers such that 1 ≤ l < r ≤ n.
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
        
    #State: The `results` list will contain either 'YES' or 'NO' for each iteration of the loop, totaling `q` elements.
    print('\n'.join(results))
    #This is printed: results (where results is a list of 'YES' or 'NO' strings, each on a new line)
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes integers t, n, q, and a list of n integers a. It then handles q queries, each defined by integers l and r. For each query, it checks if there exists a subarray within the given range [l, r] whose bitwise XOR is zero. If such a subarray exists, it appends 'YES' to the results list; otherwise, it appends 'NO'. Finally, it prints the results list, where each element is either 'YES' or 'NO', corresponding to each query.

