#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and q where 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5. The array a is a list of n integers where 0 ≤ a_i < 2^{30}. Each query is defined by l and r where 1 ≤ l < r ≤ n.
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
        
    #State: index is 6, t is an integer value from data[0], results is a list containing strings 'YES' or 'NO'.
    print('\n'.join(results))
    #This is printed: NO
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array `a` of integers, the size of the array `n`, and the number of queries `q`. For each query defined by indices `l` and `r`, the function determines if there exists a subarray within `a[l:r+1]` whose bitwise XOR is zero. If such a subarray exists, the result for that query is 'YES'; otherwise, it is 'NO'. The function collects all these results and prints them out.

