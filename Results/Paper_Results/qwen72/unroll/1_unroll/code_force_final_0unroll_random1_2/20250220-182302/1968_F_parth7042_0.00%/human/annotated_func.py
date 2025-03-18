#State of the program right berfore the function call: The function should take parameters `t`, `n`, `q`, `a`, and `queries` where `t` is an integer (1 ≤ t ≤ 10^4) representing the number of test cases, `n` and `q` are integers (2 ≤ n ≤ 2 · 10^5, 1 ≤ q ≤ 2 · 10^5) representing the number of elements in the array and the number of queries, respectively, `a` is a list of integers (0 ≤ a_i < 2^30) representing the elements of the array, and `queries` is a list of tuples (l, r) where each l and r are integers (1 ≤ l < r ≤ n) representing the query ranges. The sum of `n` over all test cases does not exceed 2 · 10^5, and the sum of `q` over all test cases does not exceed 2 · 10^5.
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
        
    #State: `t` is the integer value of `data[0]`, `n` and `q` are integers (2 ≤ n ≤ 2 · 10^5, 1 ≤ q ≤ 2 · 10^5), `a` is a list of integers (0 ≤ a_i < 2^30), `queries` is a list of tuples (l, r) where each l and r are integers (1 ≤ l < r ≤ n), `data` is a list of strings from the input, `idx` is the index after processing all the data for `t` iterations, `results` is a list containing the results of the queries for each iteration, with an empty string at the end of each iteration.
    print('\n'.join(results))
    #This is printed: sum of elements from index 1 to 2 is 5
    #sum of elements from index 2 to 3 is 9
    #
    #sum of elements from index 1 to 1 is 10
#Overall this is what the function does:The function `func_1` reads input data and processes `t` test cases. For each test case, it takes an array `a` of `n` elements and `q` queries. Each query is a tuple `(l, r)` representing a subarray range. The function determines if the XOR of the elements in the subarray `a[l-1:r]` is zero and appends 'YES' or 'NO' to the results list accordingly. After processing all queries for all test cases, it prints the results, with an empty string separating the results of different test cases. The function does not return any value; it only prints the results.

