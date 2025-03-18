#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n and q are integers where 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5; a is a list of n integers where 0 ≤ a_i < 2^30; each query consists of two integers l and r where 1 ≤ l < r ≤ n. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of q over all test cases does not exceed 2 · 10^5.
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
        
    #State: After the loop executes all iterations, `t` is 0, `n` retains the value of the last assigned `n`, `q` is 0, `idx` is increased by the total number of elements processed in `data` (which is `t * (n + 2 + q * 2)`), `a` is a list of length `n + 1` where each element from index 1 to `n` is set to the corresponding integer value from `data` for the last test case, `pf` is a list of length `n + 1` where each element from index 1 to `n` is the cumulative XOR of elements in `a` up to that index for the last test case, `mp` is a dictionary with keys being the unique values in `pf` and values being lists of indices where these `pf` values occur for the last test case, `results` contains the final results of the loop's operations ('YES' or 'NO' for each query across all test cases), and the last element of `results` is an empty string.
    print('\n'.join(results))
    #This is printed: [sequence of 'YES' or 'NO' strings, each on a new line, followed by an extra newline]
#Overall this is what the function does:The function `func_1` processes multiple test cases, each defined by the number of elements `n`, the number of queries `q`, and a list of integers `a`. It reads input data sequentially, where each test case involves calculating the XOR of subarrays and checking specific conditions based on the results. For each query, the function determines whether a certain condition related to the XOR of the subarray is met, appending 'YES' or 'NO' to the results list accordingly. After processing all queries for all test cases, it prints the results, with each result on a new line, followed by an extra newline. The function modifies the input data by consuming it and updates internal state variables but does not return any value.

