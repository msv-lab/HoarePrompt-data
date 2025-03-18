#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 2 ≤ n ≤ 2·10^5 and 1 ≤ q ≤ 2·10^5; a is a list of n integers where 0 ≤ a_i < 2^30; each query is represented by two integers l and r where 1 ≤ l < r ≤ n. The sum of n over all test cases does not exceed 2·10^5, and the sum of q over all test cases does not exceed 2·10^5.
def func_1():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        q = int(data[idx + 1])
        
        idx += 2
        
        a = [0] * (n + 1)
        
        pf = [0] * (n + 1)
        
        mp = {(0): [0]}
        
        for i in range(1, n + 1):
            a[i] = int(data[idx])
            idx += 1
            pf[i] = pf[i - 1] ^ a[i]
            if pf[i] not in mp:
                mp[pf[i]] = []
            mp[pf[i]].append(i)
        
        for _ in range(q):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
            x = pf[r] ^ pf[l - 1]
            if x == 0:
                results.append('YES')
                continue
            v1 = mp.get(pf[r], [])
            v2 = mp.get(pf[l - 1], [])
            it1 = bisect.bisect_left(v1, l)
            it2 = bisect.bisect_left(v2, r) - 1
            if it1 < len(v1) and it2 >= 0 and v1[it1] <= r and v2[it2] >= l:
                results.append('YES')
            else:
                results.append('NO')
        
        results.append('')
        
    #State: After the loop executes all iterations, `t` is 0, `idx` has been incremented by the total number of elements processed in `data` which is the sum of `n + 1 + 2 * q` for each test case, `results` contains 'YES' or 'NO' for each query based on the conditions checked within the loop, followed by an empty string for each test case. The variables `n`, `q`, `a`, `pf`, `mp`, `l`, `r`, `x`, `v1`, `v2`, `it1`, and `it2` are no longer relevant as they are re-initialized in each iteration.
    print('\n'.join(results))
    #This is printed: (Each 'YES', 'NO', or empty string from the `results` list, each on a new line)
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines whether the XOR of the subarray from index `l` to `r` is zero or if there exists a pair of indices within the subarray that have the same prefix XOR value. If either condition is met, it appends 'YES' to the results; otherwise, it appends 'NO'. After processing all queries for all test cases, it prints the results, with each result on a new line, and an additional empty line after each test case.

