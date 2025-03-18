#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. The array a contains n integers such that 0 <= a_i < 2^30 for each i. Each query is defined by two integers l and r such that 1 <= l < r <= n. The sum of n over all test cases does not exceed 2 * 10^5, and the sum of q over all test cases does not exceed 2 * 10^5.
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
        
    #State: `data` is a list of strings containing the split input values; `t` is the integer value of the first element in `data`; `index` is the position in `data` just after the last processed query; `results` is a list containing the results of all queries from all iterations.
    print('\n'.join(results))
    #This is printed: results (where results is a list of strings containing the results of all queries, joined by newline characters)
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of an array `a` and a set of queries. For each query defined by indices `l` and `r`, it determines if there exists a subarray `a[l-1:r]` whose XOR is zero and appends 'YES' or 'NO' to the results based on this condition. After processing all queries for all test cases, it prints the results, one per line.

