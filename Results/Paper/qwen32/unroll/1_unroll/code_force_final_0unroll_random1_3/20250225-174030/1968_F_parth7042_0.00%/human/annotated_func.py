#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with two integers n and q, where 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5. This is followed by a list of n integers a_1, a_2, ..., a_n, where 0 ≤ a_i < 2^30. Then, q lines follow, each containing two integers l and r, where 1 ≤ l < r ≤ n, representing the subarray a_l, a_{l+1}, ..., a_r to be queried. The sum of n over all test cases does not exceed 2 · 10^5, and the sum of q over all test cases does not exceed 2 · 10^5.
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
        
    #State: data is a list of strings representing the input values split by spaces (fully traversed); idx is the position after the last element used in the loop; t is the integer value of data[0]; results is a list containing 'YES' or 'NO' for each query, with an empty string after each test case's results.
    print('\n'.join(results))
    #This is printed: 'YES' or 'NO' on each line, followed by an empty line after each test case's results
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines if there exists a subarray within the specified range whose XOR is zero. The function outputs 'YES' if such a subarray exists and 'NO' otherwise, followed by an empty line after each test case's results.

