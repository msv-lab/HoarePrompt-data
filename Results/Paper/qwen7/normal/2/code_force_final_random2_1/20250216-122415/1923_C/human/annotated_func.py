#State of the program right berfore the function call: t is a positive integer, each test case contains n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q queries defined by pairs of integers l_i and r_i where 1 <= l_i <= r_i <= n.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = []
        
        c = 0
        
        for x in l:
            c += x
            p.append(c)
        
        for _ in range(m):
            a, b = map(int, input().split())
            s = p[b - 1]
            if a - 2 >= 0:
                s -= p[a - 2]
            if b - a + 1 > 1 and s >= 2 * (b - a + 1):
                print('YES')
            else:
                print('NO')
        
    #State: Output State: After the loop executes all iterations, `m` will be the total number of queries (q), `a` will be the last input integer for the query `a`, `b` will be the last input integer for the query `b`, and `n` will be the number of elements in the array `l`. The list `p` will contain the cumulative sums of the elements in `l` for each iteration of the loop. The variable `c` will be 0 as it is reset to 0 at the start of each iteration of the outer loop. For each query, `s` will be calculated as `p[b - 1] - p[a - 2]` if `a - 2 >= 0`, otherwise `s` will be `p[b - 1]`. If `s` is greater than or equal to `2 * (b - a + 1)`, the output will be 'YES', otherwise 'NO'. This process will repeat for all `q` queries.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the size of the array `n`, the number of queries `m`, the array `c` of length `n`, and `m` queries defined by pairs of integers `l_i` and `r_i`. It calculates the cumulative sums of the array `c` and then for each query, it determines if the sum of elements in the subarray from index `l_i` to `r_i` is at least twice the length of the subarray. If so, it prints 'YES'; otherwise, it prints 'NO'. After processing all queries for each test case, the function concludes.

