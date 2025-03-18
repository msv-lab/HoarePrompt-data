#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and q such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5. The next line contains n integers a_1,...,a_n such that 0 ≤ a_i < 2^{30}. Each query is represented by two integers l and r such that 1 ≤ l < r ≤ n.
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
        
    #State: Output State: `index` is 6; `t` is an integer value from the list `data` at position 0; `results` is a list containing alternating 'YES' and 'NO' based on the queries processed during the loop execution.
    print('\n'.join(results))
    #This is printed: YES\nNO\nYES\nNO\nYES\nNO
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer t, followed by integers n and q, and a list of n integers a_1,...,a_n. For each query (l, r), it determines whether the XOR of the subarray from index l to r is zero. If the XOR is zero, it appends 'YES' to the results list; otherwise, it appends 'NO'. After processing all queries for each test case, it prints the results list, which contains alternating 'YES' and 'NO' based on the queries processed.

