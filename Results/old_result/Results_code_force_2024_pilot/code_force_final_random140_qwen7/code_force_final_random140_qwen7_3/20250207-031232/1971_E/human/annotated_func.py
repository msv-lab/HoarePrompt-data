#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and q are integers such that k ≤ n ≤ 10^9, 1 ≤ k, q ≤ 10^5, and the sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5. a is a strictly increasing list of k integers where each integer is between 1 and n inclusive, and a[k] = n. b is a strictly increasing list of k integers where each integer is between 1 and 10^9 inclusive. d is a list of q integers where each integer is between 0 and n inclusive.
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
            m += bd[s] * ql // ad[s]
            print(m, end=' ')
        
        print()
        
    #State: The loop has executed `t` times, resulting in `i` being equal to `len(a)`, `l` being equal to `q`, and `m` being the cumulative sum of `b[s - 1] + bd[s] * (ql // ad[s])` for each iteration. The variable `ql` will be reduced by `a[s - 1]` for each iteration until it becomes zero or negative. The lists `v`, `ad`, and `bd` will remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( k \), and \( q \), along with lists \( a \) and \( b \). For each test case, it handles \( q \) queries, where each query involves finding a value based on the elements in lists \( a \) and \( b \). Specifically, for each query, it calculates and prints a cumulative sum involving elements from \( b \) and differences between consecutive elements in \( a \). After processing all queries for a test case, it moves to the next test case until all \( t \) test cases are handled. The final state includes the completion of all queries for each test case, with no explicit return values.

