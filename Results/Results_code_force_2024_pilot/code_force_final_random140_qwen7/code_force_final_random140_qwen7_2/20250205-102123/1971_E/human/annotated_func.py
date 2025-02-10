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
            m += bd[s] * ql // ad[s]
            print(m, end=' ')
        
        print()
        
    #State: The list `v` will contain `len(a) - 1` elements, each being the result of dividing the corresponding element in `ad` by the corresponding element in `bd`. The variable `i` will be set to `len(b) + 1` after the loop finishes, and `l` will be `q-1` after all iterations. The variable `m` will hold the final accumulated value of `m` after processing all inputs up to `q-1`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads integers \(n\), \(k\), and \(q\) along with two lists \(a\) and \(b\) of length \(k\). It then calculates the differences between consecutive elements in \(a\) and \(b\) and stores them in lists \(ad\) and \(bd\), respectively. Next, it computes a list \(v\) where each element is the ratio of corresponding elements in \(ad\) and \(bd\). Finally, for each query \(d_i\) (where \(0 \leq d_i \leq n\)), it finds the appropriate segment in \(a\) and calculates a value \(m\) based on the segments and prints the result. After processing all test cases, the function does not return any value but modifies internal states such as lists \(v\), \(ad\), \(bd\), and the loop variables \(i\), \(l\), and \(m\).

