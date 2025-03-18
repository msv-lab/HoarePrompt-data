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
        
    #State: Output State: `index` is 6, `t` is an integer obtained from `int(data[0])`, `data` is a list of strings obtained from splitting the input string, `results` is a list containing 'YES' or 'NO' based on the queries processed, `n` and `q` are integers obtained from `int(data[index-2])` and `int(data[index-1])` respectively, `a` is a list of `n+1` integers initialized to 0, `pf` is a list of `n+1` integers initialized to 0, `mp` is a dictionary with keys as integers and values as lists of indices, and `results` contains the answers to the queries.
    print('\n'.join(results))
    #This is printed: YES\nNO\nYES\n... (where each line represents a result from the queries processed)
#Overall this is what the function does:The function processes a series of test cases, each containing an array of integers `a` and a set of queries. For each query, it checks if there exists a subarray within the specified range `[l, r]` whose bitwise XOR is zero. If such a subarray is found, it appends 'YES' to the results; otherwise, it appends 'NO'. The function then prints the results for all queries.

