#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases, where each test case includes an array `c` of length `n` with elements greater than 0, and `q` queries. The input is provided in a specific format: the first line contains the number of test cases `t` (1 ≤ t ≤ 10^4), followed by `t` test cases. Each test case starts with two integers `n` and `q` (1 ≤ n, q ≤ 3 · 10^5), followed by `n` integers `c_1, c_2, ..., c_n` (1 ≤ c_i ≤ 10^9), and then `q` lines each containing two integers `l_i` and `r_i` (1 ≤ l_i ≤ r_i ≤ n) representing the borders of the subarray for the i-th query. The sum of `n` over all test cases does not exceed 3 · 10^5, and the sum of `q` over all test cases does not exceed 3 · 10^5.
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
        
    #State: The loop has processed all test cases. For each query, it has determined whether the sum of the subarray from `l_i` to `r_i` is at least twice the length of the subarray, and printed 'YES' or 'NO' accordingly. The variables `t`, `n`, `q`, `c`, and `l` are no longer in scope, and the final state of the program is that all input has been processed and the corresponding outputs have been printed.
#Overall this is what the function does:The function `func` processes multiple test cases, each containing an array `c` of positive integers and a set of queries. For each query, it determines whether the sum of the subarray from `l_i` to `r_i` is at least twice the length of the subarray. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function has printed the results for all queries and the input has been fully processed. The function does not return any value.

