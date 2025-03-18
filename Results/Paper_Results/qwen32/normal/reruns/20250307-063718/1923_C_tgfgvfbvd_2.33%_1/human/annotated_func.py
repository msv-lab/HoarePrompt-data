#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. The array c is a list of n integers where each element c_i satisfies 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5 and the sum of q over all test cases does not exceed 3 * 10^5.
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
        
    #State: The loop has executed `t` times, where `t` is an integer such that 1 <= t <= 10^4. For each of the `t` test cases, the following has occurred: `n` and `m` are integers where `n` is the number of elements in the list `l` and `m` is the number of queries. `l` is a list of `n` integers. `p` is a list of cumulative sums of the elements in `l`. For each of the `m` queries, `a` and `b` are integers, and based on these values, the program checks if `b - a + 1 > 1` and if `s >= 2 * (b - a + 1)`, where `s` is the sum of the elements in `l` from index `a-1` to `b-1`. If the condition is met, the program prints 'YES'; otherwise, it prints 'NO'. The state of variables `t`, `n`, `m`, `l`, `p`, and `c` is reset for each test case but remains unchanged within a single test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array of integers and a set of queries. For each query, it checks if the sum of the specified range in the array is at least twice the length of that range. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'.

