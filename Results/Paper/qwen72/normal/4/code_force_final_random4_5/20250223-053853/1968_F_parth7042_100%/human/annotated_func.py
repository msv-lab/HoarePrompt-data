#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. a is a list of n integers such that 0 <= a_i < 2^30. Each query is represented by two integers l and r such that 1 <= l < r <= n. The sum of n over all test cases does not exceed 2 * 10^5, and the sum of q over all test cases does not exceed 2 * 10^5.
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
        
    #State: `index` is the integer value of `len(data)`, `results` is a list of strings containing 'YES' or 'NO' for each query, and the values of `t`, `n`, `q`, `a`, `pf`, and `mp` are no longer relevant as they are local to the loop and will be overwritten in each iteration.
    print('\n'.join(results))
    #This is printed: [each element of results on a new line, where each element is either 'YES' or 'NO']
#Overall this is what the function does:The function `func_1` processes a series of test cases. Each test case involves a list of integers `a` and a set of queries. For each query, the function determines if the XOR of the subarray `a[l]` to `a[r]` is zero or if there exists a valid subarray within the range that results in a zero XOR. The function prints 'YES' for each query where the condition is met, and 'NO' otherwise. After processing all test cases, the function has no return value, but the output is a series of 'YES' or 'NO' responses, each on a new line, corresponding to the queries. The state of the program after the function concludes is that the input data has been fully processed, and the results of the queries have been printed.

