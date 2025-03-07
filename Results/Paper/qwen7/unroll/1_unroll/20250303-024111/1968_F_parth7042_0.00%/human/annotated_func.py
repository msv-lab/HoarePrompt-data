#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 2 \le n \le 2 \cdot 10^5 and 1 \le q \le 2 \cdot 10^5. The array a consists of n integers where 0 \le a_i < 2^{30}. Each query is defined by two integers l and r such that 1 \le l < r \le n.
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
        
    #State: Output State: `t` is an integer value from `data[idx]`, `data` is a list of strings obtained from splitting the input, `idx` is greater than the original value, `results` is a list containing multiple 'YES' and 'NO' strings based on the conditions checked within the loop, `results` ends with an empty string.
    print('\n'.join(results))
    #This is printed: YES\nNO\n...\n
#Overall this is what the function does:The function processes multiple test cases, each involving an array `a` of integers and a set of queries defined by pairs of indices `l` and `r`. For each query, it checks if the XOR of the subarray from index `l` to `r-1` is zero or if there exists a subarray within the specified range whose XOR is zero. If either condition is met, it appends 'YES' to the results; otherwise, it appends 'NO'. After processing all queries for each test case, it appends an empty string to the results list. Finally, it prints the results as a sequence of 'YES' and 'NO' strings, separated by newlines.

