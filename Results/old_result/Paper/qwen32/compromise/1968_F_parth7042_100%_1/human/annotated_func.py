#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. The array a contains n integers where each integer a_i satisfies 0 <= a_i < 2^30. Each query is defined by two integers l and r such that 1 <= l < r <= n. The sum of n over all test cases does not exceed 2 * 10^5 and the sum of q over all test cases does not exceed 2 * 10^5.
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
        
    #State: `t` is `0`; `n` is the integer value of `data[index]` from the last iteration; `q` is the integer value of `data[index + 1]` from the last iteration; `a` is a list of `n + 1` elements where `a[0]` is `0` and `a[i]` for `i` from `1` to `n` are the integers read from `data` starting at `index + 2`; `data` is unchanged; `index` is the final index after processing all `n` and `q` values; `results` is a list containing the results of all queries from all iterations; `pf` is a list of `n + 1` elements where `pf[0]` is `0` and `pf[i]` for `i` from `1` to `n` are the cumulative XOR values of `a` up to that index; `mp` is a defaultdict where each key is a unique XOR value in `pf` and maps to a list of indices where that XOR value was achieved.
    print('\n'.join(results))
    #This is printed: The contents of the `results` list, each element separated by a newline character
#Overall this is what the function does:The function `func_1` processes multiple test cases. Each test case consists of an integer `n`, an integer `q`, an array `a` of `n` integers, and `q` queries. Each query is defined by two integers `l` and `r`. The function determines for each query whether there exists a subarray within the range `[l, r]` such that the XOR of all its elements is zero. The results of these queries are printed, one per line.

