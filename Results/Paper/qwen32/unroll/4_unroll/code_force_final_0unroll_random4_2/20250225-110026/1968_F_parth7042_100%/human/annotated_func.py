#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. a is a list of n integers where each integer a_i satisfies 0 <= a_i < 2^30. Each of the q queries is a pair of integers (l, r) such that 1 <= l < r <= n. The sum of n over all test cases does not exceed 2 * 10^5, and the sum of q over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is an integer such that 1 <= t <= 10^4; for each test case, `n` and `q` are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5; `a` is a list of `n` integers where each integer `a_i` satisfies 0 <= `a_i` < 2^30; each of the `q` queries is a pair of integers (l, r) such that 1 <= l < r <= n; the sum of `n` over all test cases does not exceed 2 * 10^5, and the sum of `q` over all test cases does not exceed 2 * 10^5; `data` is a list of strings obtained by splitting the input line; `index` is 1 plus twice the total number of test cases plus the sum of `n` for all test cases; `results` is a list of strings 'YES' or 'NO' corresponding to the answers of the queries for all test cases.`
    print('\n'.join(results))
    #This is printed: 'YES' or 'NO' for each query, each on a new line (where 'YES' or 'NO' corresponds to the answers of the queries for all test cases)
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it receives a list of integers and a series of queries. Each query asks whether there exists a subarray within the specified range that has a bitwise XOR of zero. The function outputs 'YES' if such a subarray exists and 'NO' otherwise, for each query.

