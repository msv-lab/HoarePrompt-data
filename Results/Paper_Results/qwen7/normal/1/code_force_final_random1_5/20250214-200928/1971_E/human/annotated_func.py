#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and q are integers such that k ≤ n ≤ 10^9, 1 ≤ k, q ≤ 10^5, and the sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5. a is a list of k integers where 1 ≤ a_i ≤ n and a_i < a_{i+1} for every 1 ≤ i ≤ k-1, and a_k = n. b is a list of k integers where 1 ≤ b_i ≤ 10^9 and b_i < b_{i+1} for every 1 ≤ i ≤ k-1. d is a list of q integers where 0 ≤ d ≤ n.
def func():
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        
        a = [0] + list(map(int, input().split()))
        
        b = [0] + list(map(int, input().split()))
        
        ad = [0]
        
        bd = [0]
        
        for i in range(1, len(a)):
            ad.append(a[i] - a[i - 1])
        
        for i in range(1, len(b)):
            bd.append(b[i] - b[i - 1])
        
        v = [0]
        
        for i in range(1, len(a)):
            v.append(ad[i] / bd[i])
        
        for l in range(q):
            m = 0
            i = 1
            ql = int(input())
            s = bisect_left(a, ql)
            if a[s] == ql:
                print(b[s], end=' ')
                continue
            ql -= a[s - 1]
            m += b[s - 1]
            m += bd[s] * ql / ad[s]
            print(int(m), end=' ')
        
        print()
        
    #State: Output State: After the loop executes all its iterations, the following conditions will be true:
    #
    #- The variable `l` will be set to `q - 1`.
    #- The variable `i` will remain 1 throughout the loop.
    #- The variable `m` will contain the final cumulative sum after processing all inputs. This sum starts with `b[s - 1]` and adds the scaled values from `bd[s]` for each iteration, calculated as `bd[s] * (ql - a[s - 1]) / ad[s]`.
    #- The list `v` will be a list of length `len(a)` where the first element is `0` and the rest are the results of dividing corresponding elements of `ad` by `bd`.
    #- The variable `t` will be unchanged, representing the number of test cases.
    #- The lists `a` and `b` will retain their original values after processing all queries.
    #- The variable `ad` and `bd` will contain the differences between consecutive elements of `a` and `b`, respectively, up to the last valid index.
    #
    #In simpler terms, after all iterations of the loop, `l` will be `q-1`, `i` will stay as 1, `m` will hold the final calculated value after processing all inputs, `v` will contain the ratios of differences, and `a`, `b`, `ad`, and `bd` will keep their processed values but will not change further within the loop.
#Overall this is what the function does:The function processes multiple test cases, each involving two lists of integers `a` and `b`. For each test case, it handles `q` queries, where each query involves finding a specific value `ql` within the range defined by `a`. Based on the position of `ql` in `a`, it calculates and prints a corresponding value derived from `b` using linear interpolation between the relevant elements of `b`. After processing all queries for a test case, it outputs the final calculated value `m` for each query. The function retains the original values of `a`, `b`, and other lists after processing all queries.

