#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n and q are integers where 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5, a is a list of integers where 0 ≤ a_i < 2^30, and each query consists of two integers l and r where 1 ≤ l < r ≤ n. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of q over all test cases does not exceed 2 · 10^5.
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
        
    #State: `index` is `1 + 2 * t + 2 * (n + q)`, and `results` is a list of strings containing 'YES' or 'NO' for each query.
    print('\n'.join(results))
    #This is printed: 'YES' or 'NO' (each on a new line, corresponding to the elements in the `results` list)
#Overall this is what the function does:The function `func_1` reads input data, processes multiple test cases, and determines for each query whether the XOR of the elements in the specified subarray of `a` is zero or if there exists a subarray with the same XOR value that can be swapped to make the XOR zero. It prints 'YES' or 'NO' for each query, with each result on a new line. The function does not return any value; it only prints the results. After the function concludes, the `index` variable is updated to `1 + 2 * t + 2 * (n + q)`, and the `results` list contains the results of all queries.

