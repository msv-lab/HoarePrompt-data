#State of the program right berfore the function call: t is a positive integer, and each test case consists of two integers n and q where 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5. The next line contains n integers a_1,...,a_n where 0 ≤ a_i < 2^{30}. Each of the next q lines contains two integers l and r where 1 ≤ l < r ≤ n.
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
        
    #State: After the loop executes all iterations, `t` will be 0, `n` will retain its final value from the last iteration, `q` will be 0, `index` will be equal to its initial value plus twice the total number of iterations (i.e., `2 * t`), and `results` will contain 'YES' or 'NO' appended based on the conditions evaluated within the loop for all `q` queries.
    print('\n'.join(results))
    #This is printed: ""
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array of integers and a series of range queries. For each test case, it calculates the bitwise XOR of subarrays defined by the query ranges and determines whether the result is zero. If the result is zero, it appends 'YES' to the results list; otherwise, it appends 'NO'. After processing all test cases and queries, it prints the results list, which contains 'YES' or 'NO' for each query.

