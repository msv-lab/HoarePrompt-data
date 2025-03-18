#State of the program right berfore the function call: The function `func_1` is incomplete and does not match the problem description. The correct function definition should be `def func_1(t, test_cases):` where `t` is an integer representing the number of test cases, and `test_cases` is a list of tuples, each containing integers `n`, `q`, a list `a` of integers, and a list of `q` queries, each query being a tuple of two integers `l` and `r`. For each test case, `n` and `q` satisfy 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5, respectively, and for each query, `l` and `r` satisfy 1 ≤ l < r ≤ n. The elements of `a` are integers in the range 0 ≤ a_i < 2^30. The sum of `n` and the sum of `q` over all test cases do not exceed 2 · 10^5.
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
        
    #State: The loop has completed all `t` iterations, `index` is `3 * t + 2 * (sum of all `n` values) + 2 * (sum of all `q` values)`, `results` is a list of length `sum of all `q` values` where each element is either 'YES' or 'NO' based on the conditions checked in each query iteration.
    print('\n'.join(results))
    #This is printed: - Since the exact values of 'YES' or 'NO' in the `results` list are not provided, we can only describe the output in terms of the structure of the list.
    #   - The output will be a series of 'YES' or 'NO' strings, each on a new line, corresponding to the elements in the `results` list.
    #
    #Output:
#Overall this is what the function does:The function `func_1` reads input data, processes multiple test cases, and prints the results. It accepts no parameters and returns no values. Each test case includes an integer `n`, an integer `q`, a list `a` of integers, and a list of `q` queries, each query being a tuple of two integers `l` and `r`. For each query, the function determines if the XOR of the subarray `a[l]` to `a[r]` is zero or if there exist indices `i` and `j` such that `l ≤ i < j ≤ r` and the XOR of the subarray `a[i+1]` to `a[j]` is zero. If either condition is met, the function appends 'YES' to the results list; otherwise, it appends 'NO'. After processing all test cases, the function prints the results, with each result on a new line.

