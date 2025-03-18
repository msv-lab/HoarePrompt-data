#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of integers of length n representing the sorted prefix sums of array a, where each element in p satisfies |p_i| <= n.
def func_1(n, p):
    dp = [0] * (2 * n + 1)
    offset = n
    dp[offset] = 1
    for i in range(1, n + 1):
        new_dp = [0] * (2 * n + 1)
        
        for j in range(2 * n + 1):
            if dp[j] > 0:
                if j + 1 <= 2 * n:
                    new_dp[j + 1] = (new_dp[j + 1] + dp[j]) % MOD
                if j - 1 >= 0:
                    new_dp[j - 1] = (new_dp[j - 1] + dp[j]) % MOD
        
        dp = new_dp
        
    #State: `n` is a positive integer (at least 1); `p` is a list of integers of length `n`; `dp` is a list of integers of length `2 * n + 1` where each element `dp[j]` is the binomial coefficient `C(n, j-n) % MOD`; `offset` is `n`; `i` is `n + 1`.
    final_sum = p[-1] + offset
    return dp[final_sum]
    #The program returns `dp[p[-1] + n]`, which is the binomial coefficient `C(n, p[-1]) % MOD`.
#Overall this is what the function does:The function calculates and returns the binomial coefficient \( C(n, p[-1]) \) modulo `MOD`, where `n` is a positive integer and `p` is a list of integers of length `n` representing the sorted prefix sums of an array `a`.

#State of the program right berfore the function call: n is a positive integer representing the size of the hidden array a, and p is a list of n integers representing the sorted prefix sums of array a, where |p_i| <= n for each element p_i in p.
def func_2():
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        
        index += 1
        
        p = list(map(int, data[index:index + n]))
        
        index += n
        
        result = func_1(n, p)
        
        results.append(result)
        
    #State: `n` is the integer value of `data[1 + (t-1)*(n+1)]`, `p` is a list of integers from `data[2 + (t-1)*(n+1)]` to `data[1 + t*(n+1)]`, `data` is a list of strings obtained by splitting the `input` content by whitespace, `index` is `1 + t * (n + 1)`, `t` is the integer value of `data[0]`, `results` is a list containing `t` elements, each being the value of `result` from each iteration.
    for res in results:
        print(res)
        
    #State: All elements in `results` have been printed.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n` and a list `p` of `n` integers. It processes each test case using another function `func_1` to compute a result, collects these results, and prints each one.

